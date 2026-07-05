#!/usr/bin/env python
"""
Búsqueda de hiperparámetros propia para XGBoost (LPMC).

Metodología común con Random Forest (04_tune_rf.py): optimización Bayesiana con
HyperOpt (TPE) sobre el conjunto de entrenamiento, validación cruzada estratificada
y agrupada por household_id (k=5), objetivo = entropía cruzada media en validación.

Esta búsqueda propia sirve como referencia. Para el modelo XGBoost final se adoptan
los hiperparámetros de la investigación de referencia del tutor (búsqueda de 1000
evaluaciones), que se guardan en lpmc_xgb_best_params.json.

Entrada : data/preprocessed/LPMC_train.csv
Salida  : artifacts/lpmc_xgb_custom_params.json

Variables de entorno:
  XGB_MAX_EVALS  — evaluaciones de HyperOpt (por defecto 100)
  XGB_SAMPLE     — fracción del train usada (por defecto 1.0, conjunto completo)

Uso:
    python 03_tune_xgb.py
"""

import json
import os
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data" / "preprocessed"
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)

RANDOM_STATE = 481516
CV = 5
MAX_EVALS = int(os.environ.get("XGB_MAX_EVALS", "100"))
SAMPLE_FRAC = float(os.environ.get("XGB_SAMPLE", "1.0"))

SCALED_FEATURES = [
    "day_of_week", "start_time_linear", "age", "car_ownership", "distance",
    "dur_walking", "dur_cycling", "dur_pt_access", "dur_pt_rail", "dur_pt_bus",
    "dur_pt_int_waiting", "dur_pt_int_walking", "pt_n_interchanges", "dur_driving",
    "cost_transit", "cost_driving_total",
]


def stratified_group_k_fold(y, groups, k, seed=None):
    labels_num = int(np.max(y)) + 1
    y_counts_per_group = defaultdict(lambda: np.zeros(labels_num))
    y_distr = Counter()
    for label, g in zip(y, groups):
        y_counts_per_group[g][label] += 1
        y_distr[label] += 1
    y_counts_per_fold = defaultdict(lambda: np.zeros(labels_num))
    groups_per_fold = defaultdict(set)

    def eval_fold(y_counts, fold):
        y_counts_per_fold[fold] += y_counts
        std_per_label = [np.std([y_counts_per_fold[i][label] / y_distr[label] for i in range(k)])
                         for label in range(labels_num)]
        y_counts_per_fold[fold] -= y_counts
        return np.mean(std_per_label)

    items = list(y_counts_per_group.items())
    rng = np.random.default_rng(seed)
    rng.shuffle(items)
    for g, y_counts in sorted(items, key=lambda x: -np.std(x[1])):
        best_fold, min_eval = None, None
        for i in range(k):
            fe = eval_fold(y_counts, i)
            if min_eval is None or fe < min_eval:
                min_eval, best_fold = fe, i
        y_counts_per_fold[best_fold] += y_counts
        groups_per_fold[best_fold].add(g)
    all_groups = set(groups)
    for i in range(k):
        tr = [idx for idx, g in enumerate(groups) if g in (all_groups - groups_per_fold[i])]
        te = [idx for idx, g in enumerate(groups) if g in groups_per_fold[i]]
        yield tr, te


def main() -> None:
    from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
    from xgboost import XGBClassifier

    train = pd.read_csv(DATA_DIR / "LPMC_train.csv")
    y_full = train["travel_mode"].astype(int)
    X_full = train.drop(columns=["travel_mode"])
    scaled_features = [c for c in SCALED_FEATURES if c in X_full.columns]

    rng = np.random.default_rng(RANDOM_STATE)
    if SAMPLE_FRAC < 1.0:
        idx = rng.choice(len(X_full), size=int(len(X_full) * SAMPLE_FRAC), replace=False)
        X_full = X_full.iloc[idx].reset_index(drop=True)
        y_full = y_full.iloc[idx].reset_index(drop=True)
    groups = np.array(X_full["household_id"].values)
    X = X_full.drop(columns=["household_id"]).reset_index(drop=True)
    y = y_full.reset_index(drop=True)
    print(f"Conjunto de búsqueda ({SAMPLE_FRAC:.0%}): {X.shape}; {MAX_EVALS} evals, {CV}-fold CV")

    folds = list(stratified_group_k_fold(y.values, groups, k=CV, seed=RANDOM_STATE))

    space = {
        "max_depth": hp.quniform("max_depth", 3, 10, 1),
        "gamma": hp.loguniform("gamma", -5, 1),
        "min_child_weight": hp.quniform("min_child_weight", 1, 50, 1),
        "subsample": hp.uniform("subsample", 0.5, 0.9),
        "colsample_bytree": hp.uniform("colsample_bytree", 0.5, 1.0),
        "reg_alpha": hp.loguniform("reg_alpha", -7, 1),
        "reg_lambda": hp.loguniform("reg_lambda", -7, 1),
        "n_estimators": hp.quniform("n_estimators", 300, 1000, 50),
        "learning_rate": hp.uniform("learning_rate", 0.02, 0.2),
    }

    def to_params(s):
        p = {k: (int(v) if k in ("max_depth", "min_child_weight", "n_estimators") else float(v))
             for k, v in s.items()}
        p.update({"objective": "multi:softprob", "eval_metric": "mlogloss",
                  "num_class": 4, "n_jobs": -1, "random_state": RANDOM_STATE})
        return p

    def objective(s):
        params = to_params(s)
        loss, n = 0.0, 0
        for tr_idx, te_idx in folds:
            X_tr, X_te = X.loc[tr_idx].copy(), X.loc[te_idx].copy()
            sc = StandardScaler()
            X_tr[scaled_features] = sc.fit_transform(X_tr[scaled_features].astype(float))
            X_te[scaled_features] = sc.transform(X_te[scaled_features].astype(float))
            clf = XGBClassifier(**params)
            clf.fit(X_tr, y.loc[tr_idx])
            proba = np.clip(clf.predict_proba(X_te), 1e-12, 1.0)
            yte = y.loc[te_idx].values
            loss -= np.log(proba[np.arange(len(yte)), yte]).sum()
            n += len(yte)
        return {"loss": loss / n, "status": STATUS_OK}

    print(f"\nLanzando búsqueda HyperOpt/TPE...")
    trials = Trials()
    best = fmin(fn=objective, space=space, algo=tpe.suggest, max_evals=MAX_EVALS,
                trials=trials, rstate=np.random.default_rng(RANDOM_STATE))
    best_params = to_params({
        "max_depth": best["max_depth"], "gamma": best["gamma"],
        "min_child_weight": best["min_child_weight"], "subsample": best["subsample"],
        "colsample_bytree": best["colsample_bytree"], "reg_alpha": best["reg_alpha"],
        "reg_lambda": best["reg_lambda"], "n_estimators": best["n_estimators"],
        "learning_rate": best["learning_rate"],
    })
    best_loss = min(t["result"]["loss"] for t in trials.trials)
    print(f"\nMejor CE={best_loss:.4f}  GMPCA~={np.exp(-best_loss):.4f}")
    for k, v in best_params.items():
        print(f"  {k}: {v}")

    payload = {
        "source": "03_tune_xgb.py (HyperOpt/TPE, conjunto de entrenamiento completo)",
        "cv": CV, "max_evals": MAX_EVALS, "sample_frac": SAMPLE_FRAC,
        "best_cv_gmpca": float(np.exp(-best_loss)),
        "params": best_params, "scaled_features": scaled_features,
    }
    (ARTIFACTS / "lpmc_xgb_custom_params.json").write_text(json.dumps(payload, indent=2))
    print(f"\nGuardado en: {ARTIFACTS / 'lpmc_xgb_custom_params.json'}")


if __name__ == "__main__":
    main()
