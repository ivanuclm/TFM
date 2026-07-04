#!/usr/bin/env python
"""
Búsqueda de hiperparámetros propia para el Random Forest (LPMC).

Metodología idéntica a la búsqueda de XGBoost (notebooks/03_tune_xgb.ipynb) para
que ambos modelos sean comparables: muestra del 25% del conjunto de entrenamiento,
validación cruzada estratificada y agrupada por household_id (k=5) y optimización
Bayesiana con HyperOpt (TPE). La función objetivo es la entropía cruzada media en
los folds de validación (equivalente a minimizar -log GMPCA).

A diferencia de XGBoost (donde se dispone de la búsqueda exhaustiva de 1000
evaluaciones del tutor), para Random Forest no existe una referencia externa, por
lo que la mejor configuración encontrada aquí es la que se adopta para el modelo
final si mejora la configuración manual de partida.

Entrada : data/preprocessed/LPMC_train.csv
Salida  : artifacts/lpmc_rf_custom_params.json

Variables de entorno:
  RF_MAX_EVALS  — número de evaluaciones de HyperOpt (por defecto 40)
  RF_SAMPLE     — fracción del train usada en la búsqueda (por defecto 0.25)

Uso:
    python 04_tune_rf.py
"""

import json
import os
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data" / "preprocessed"
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)

RANDOM_STATE = 481516
CV = 5
MAX_EVALS = int(os.environ.get("RF_MAX_EVALS", "40"))
SAMPLE_FRAC = float(os.environ.get("RF_SAMPLE", "0.25"))

SCALED_FEATURES = [
    "day_of_week", "start_time_linear", "age", "car_ownership", "distance",
    "dur_walking", "dur_cycling", "dur_pt_access", "dur_pt_rail", "dur_pt_bus",
    "dur_pt_int_waiting", "dur_pt_int_walking", "pt_n_interchanges", "dur_driving",
    "cost_transit", "cost_driving_total",
]


def stratified_group_k_fold(y, groups, k, seed=None):
    """Stratified Group K-Fold (misma implementación que la búsqueda de XGBoost)."""
    labels_num = int(np.max(y)) + 1
    y_counts_per_group = defaultdict(lambda: np.zeros(labels_num))
    y_distr = Counter()
    for label, g in zip(y, groups):
        y_counts_per_group[g][label] += 1
        y_distr[label] += 1

    y_counts_per_fold = defaultdict(lambda: np.zeros(labels_num))
    groups_per_fold = defaultdict(set)

    def eval_y_counts_per_fold(y_counts, fold):
        y_counts_per_fold[fold] += y_counts
        std_per_label = []
        for label in range(labels_num):
            label_std = np.std([y_counts_per_fold[i][label] / y_distr[label] for i in range(k)])
            std_per_label.append(label_std)
        y_counts_per_fold[fold] -= y_counts
        return np.mean(std_per_label)

    groups_and_y_counts = list(y_counts_per_group.items())
    rng = np.random.default_rng(seed)
    rng.shuffle(groups_and_y_counts)

    for g, y_counts in sorted(groups_and_y_counts, key=lambda x: -np.std(x[1])):
        best_fold, min_eval = None, None
        for i in range(k):
            fold_eval = eval_y_counts_per_fold(y_counts, i)
            if min_eval is None or fold_eval < min_eval:
                min_eval, best_fold = fold_eval, i
        y_counts_per_fold[best_fold] += y_counts
        groups_per_fold[best_fold].add(g)

    all_groups = set(groups)
    for i in range(k):
        train_groups = all_groups - groups_per_fold[i]
        test_groups = groups_per_fold[i]
        train_idx = [idx for idx, g in enumerate(groups) if g in train_groups]
        test_idx = [idx for idx, g in enumerate(groups) if g in test_groups]
        yield train_idx, test_idx


def main() -> None:
    from hyperopt import STATUS_OK, Trials, fmin, hp, tpe

    train = pd.read_csv(DATA_DIR / "LPMC_train.csv")
    target_col = "travel_mode"
    X_full = train.drop(columns=[target_col])
    y_full = train[target_col].astype(int)
    print(f"Train completo: {X_full.shape}")

    scaled_features = [c for c in SCALED_FEATURES if c in X_full.columns]

    rng = np.random.default_rng(RANDOM_STATE)
    sample_idx = rng.choice(len(X_full), size=int(len(X_full) * SAMPLE_FRAC), replace=False)
    X_sample = X_full.iloc[sample_idx].reset_index(drop=True)
    y_sample = y_full.iloc[sample_idx].reset_index(drop=True)
    groups = np.array(X_sample["household_id"].values)
    X_sample = X_sample.drop(columns=["household_id"])
    print(f"Muestra de búsqueda ({SAMPLE_FRAC:.0%}): {X_sample.shape}")

    folds = list(stratified_group_k_fold(y_sample.values, groups, k=CV, seed=RANDOM_STATE))

    space = {
        "n_estimators": hp.quniform("n_estimators", 200, 700, 50),
        "max_depth": hp.choice("max_depth", [None, 12, 20, 30, 40]),
        "min_samples_split": hp.quniform("min_samples_split", 2, 20, 1),
        "min_samples_leaf": hp.quniform("min_samples_leaf", 1, 10, 1),
        "max_features": hp.choice("max_features", ["sqrt", "log2", 0.5]),
    }

    def to_params(s):
        return {
            "n_estimators": int(s["n_estimators"]),
            "max_depth": s["max_depth"],
            "min_samples_split": int(s["min_samples_split"]),
            "min_samples_leaf": int(s["min_samples_leaf"]),
            "max_features": s["max_features"],
            "n_jobs": -1,
            "random_state": RANDOM_STATE,
        }

    def objective(s):
        params = to_params(s)
        loss, n_total = 0.0, 0
        for tr_idx, te_idx in folds:
            X_tr = X_sample.loc[tr_idx].copy()
            X_te = X_sample.loc[te_idx].copy()
            y_tr = y_sample.loc[tr_idx]
            y_te = y_sample.loc[te_idx].values

            scaler = StandardScaler()
            X_tr[scaled_features] = scaler.fit_transform(X_tr[scaled_features].astype(float))
            X_te[scaled_features] = scaler.transform(X_te[scaled_features].astype(float))

            clf = RandomForestClassifier(**params)
            clf.fit(X_tr, y_tr)
            proba = np.clip(clf.predict_proba(X_te), 1e-12, 1.0)
            loss -= np.log(proba[np.arange(len(y_te)), y_te]).sum()
            n_total += len(y_te)
        return {"loss": loss / n_total, "status": STATUS_OK}

    print(f"\nLanzando búsqueda HyperOpt/TPE: {MAX_EVALS} evaluaciones, {CV}-fold CV...")
    trials = Trials()
    best = fmin(
        fn=objective, space=space, algo=tpe.suggest, max_evals=MAX_EVALS,
        trials=trials, rstate=np.random.default_rng(RANDOM_STATE),
    )

    # fmin con hp.choice devuelve índices; reconstruir los valores reales.
    depth_opts = [None, 12, 20, 30, 40]
    feat_opts = ["sqrt", "log2", 0.5]
    best_params = {
        "n_estimators": int(best["n_estimators"]),
        "max_depth": depth_opts[best["max_depth"]],
        "min_samples_split": int(best["min_samples_split"]),
        "min_samples_leaf": int(best["min_samples_leaf"]),
        "max_features": feat_opts[best["max_features"]],
        "n_jobs": -1,
        "random_state": RANDOM_STATE,
    }
    best_loss = min(t["result"]["loss"] for t in trials.trials)
    print(f"\nMejor configuración encontrada (CE={best_loss:.4f}, GMPCA~={np.exp(-best_loss):.4f}):")
    for k, v in best_params.items():
        print(f"  {k}: {v}")

    serializable = {k: (str(v) if v is None else v) for k, v in best_params.items()}
    payload = {
        "source": "04_tune_rf.py",
        "cv": CV,
        "max_evals": MAX_EVALS,
        "sample_frac": SAMPLE_FRAC,
        "best_cv_gmpca": float(np.exp(-best_loss)),
        "params": serializable,
        "scaled_features": scaled_features,
    }
    out_path = ARTIFACTS / "lpmc_rf_custom_params.json"
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"\nHiperparámetros propios guardados en: {out_path}")


if __name__ == "__main__":
    main()
