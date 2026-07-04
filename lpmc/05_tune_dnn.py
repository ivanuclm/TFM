#!/usr/bin/env python
"""
Búsqueda de hiperparámetros propia para la red neuronal profunda (DNN, LPMC).

A diferencia de los modelos de árbol, cada evaluación de la DNN exige un ciclo
completo de entrenamiento, por lo que una búsqueda Bayesiana de cientos de
evaluaciones resultaría prohibitiva en CPU. Se opta por una búsqueda aleatoria
acotada: se muestrean varias configuraciones del espacio de hiperparámetros
(tasa de aprendizaje, tamaños de capa, dropout, weight_decay y tamaño de lote) y
se evalúa cada una con validación cruzada agrupada por household_id. La métrica
de selección es la entropía cruzada media en validación (equivale a maximizar el
GMPCA). El entrenamiento de cada configuración se acorta (menos épocas y CV de 3
folds) por tratarse de una exploración, no del entrenamiento final.

Entrada : data/preprocessed/LPMC_train.csv
Salida  : artifacts/lpmc_dnn_custom_params.json

Variables de entorno:
  DNN_TUNE_CONFIGS — número de configuraciones a muestrear (por defecto 12)
  DNN_TUNE_EPOCHS  — épocas máximas por evaluación (por defecto 40)
  DNN_TUNE_SAMPLE  — fracción del train usada en la búsqueda (por defecto 0.5)

Uso:
    python 05_tune_dnn.py
"""

import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data" / "preprocessed"
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)

RANDOM_STATE = 481516
CV = 3
N_CONFIGS = int(os.environ.get("DNN_TUNE_CONFIGS", "12"))
MAX_EPOCHS = int(os.environ.get("DNN_TUNE_EPOCHS", "40"))
SAMPLE_FRAC = float(os.environ.get("DNN_TUNE_SAMPLE", "0.5"))

SCALED_FEATURES = [
    "day_of_week", "start_time_linear", "age", "car_ownership", "distance",
    "dur_walking", "dur_cycling", "dur_pt_access", "dur_pt_rail", "dur_pt_bus",
    "dur_pt_int_waiting", "dur_pt_int_walking", "pt_n_interchanges", "dur_driving",
    "cost_transit", "cost_driving_total",
]

# Espacio de búsqueda discreto. La arquitectura de partida (128,64,32) es la
# configuración manual desplegada; se exploran variantes más anchas y más estrechas.
SEARCH_SPACE = {
    "hidden": [(128, 64, 32), (256, 128, 64), (64, 32, 16), (128, 128, 64)],
    "lr": [3e-3, 1e-3, 5e-4],
    "dropout": [(0.3, 0.2), (0.4, 0.3), (0.2, 0.1)],
    "weight_decay": [1e-3, 1e-4],
    "batch_size": [256, 512],
}


def build_model(n_features, hidden, dropout):
    import torch.nn as nn
    h1, h2, h3 = hidden
    d1, d2 = dropout
    return nn.Sequential(
        nn.Linear(n_features, h1), nn.BatchNorm1d(h1), nn.ReLU(), nn.Dropout(d1),
        nn.Linear(h1, h2), nn.BatchNorm1d(h2), nn.ReLU(), nn.Dropout(d2),
        nn.Linear(h2, h3), nn.BatchNorm1d(h3), nn.ReLU(),
        nn.Linear(h3, 4),
    )


def train_eval(cfg, X_tr, y_tr, X_val, y_val, n_features):
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader, TensorDataset

    torch.manual_seed(RANDOM_STATE)
    model = build_model(n_features, cfg["hidden"], cfg["dropout"])
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg["lr"], weight_decay=cfg["weight_decay"])
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, factor=0.5, patience=4, min_lr=1e-5)
    criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

    X_tr_t = torch.tensor(X_tr, dtype=torch.float32)
    y_tr_t = torch.tensor(y_tr, dtype=torch.long)
    X_val_t = torch.tensor(X_val, dtype=torch.float32)
    y_val_t = torch.tensor(y_val, dtype=torch.long)
    loader = DataLoader(TensorDataset(X_tr_t, y_tr_t), batch_size=cfg["batch_size"], shuffle=True)

    best_val, patience_counter, patience = float("inf"), 0, 6
    for _ in range(MAX_EPOCHS):
        model.train()
        for Xb, yb in loader:
            optimizer.zero_grad()
            criterion(model(Xb), yb).backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
        model.eval()
        with torch.no_grad():
            val_loss = criterion(model(X_val_t), y_val_t).item()
        scheduler.step(val_loss)
        if val_loss < best_val:
            best_val, patience_counter = val_loss, 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                break

    # Entropía cruzada real (sin label smoothing) para comparar configuraciones.
    import torch.nn.functional as F
    model.eval()
    with torch.no_grad():
        proba = F.softmax(model(X_val_t), dim=1).numpy()
    proba = np.clip(proba, 1e-12, 1.0)
    ce = -np.log(proba[np.arange(len(y_val)), y_val]).mean()
    return float(ce)


def main() -> None:
    train = pd.read_csv(DATA_DIR / "LPMC_train.csv")
    target_col = "travel_mode"
    y_full = train[target_col].astype(int)
    X_full = train.drop(columns=[target_col])

    scaled_features = [c for c in SCALED_FEATURES if c in X_full.columns]

    rng = np.random.default_rng(RANDOM_STATE)
    sample_idx = rng.choice(len(X_full), size=int(len(X_full) * SAMPLE_FRAC), replace=False)
    X_sample = X_full.iloc[sample_idx].reset_index(drop=True)
    y_sample = y_full.iloc[sample_idx].reset_index(drop=True)
    groups = X_sample["household_id"].values
    X_sample = X_sample.drop(columns=["household_id"])
    n_features = X_sample.shape[1]
    print(f"Muestra de búsqueda ({SAMPLE_FRAC:.0%}): {X_sample.shape}; configs={N_CONFIGS}, epochs={MAX_EPOCHS}")

    # Muestrear N_CONFIGS combinaciones distintas del espacio.
    keys = list(SEARCH_SPACE.keys())
    seen, configs = set(), []
    while len(configs) < N_CONFIGS and len(seen) < np.prod([len(SEARCH_SPACE[k]) for k in keys]):
        cfg = {k: SEARCH_SPACE[k][rng.integers(len(SEARCH_SPACE[k]))] for k in keys}
        sig = tuple(str(cfg[k]) for k in keys)
        if sig in seen:
            continue
        seen.add(sig)
        configs.append(cfg)

    gkf = GroupKFold(n_splits=CV)
    fold_idx = list(gkf.split(X_sample, y_sample, groups))

    results = []
    for i, cfg in enumerate(configs, start=1):
        ces = []
        for tr_idx, val_idx in fold_idx:
            Xf_tr, Xf_val = X_sample.iloc[tr_idx].copy(), X_sample.iloc[val_idx].copy()
            sc = StandardScaler()
            Xf_tr[scaled_features] = sc.fit_transform(Xf_tr[scaled_features].astype(float))
            Xf_val[scaled_features] = sc.transform(Xf_val[scaled_features].astype(float))
            ce = train_eval(
                cfg, Xf_tr.values.astype(np.float32), y_sample.iloc[tr_idx].values,
                Xf_val.values.astype(np.float32), y_sample.iloc[val_idx].values, n_features,
            )
            ces.append(ce)
        mean_ce = float(np.mean(ces))
        results.append((mean_ce, cfg))
        print(f"  [{i}/{len(configs)}] CE={mean_ce:.4f} GMPCA~={np.exp(-mean_ce):.4f}  {cfg}")

    results.sort(key=lambda x: x[0])
    best_ce, best_cfg = results[0]
    print(f"\nMejor configuración (CE={best_ce:.4f}, GMPCA~={np.exp(-best_ce):.4f}):")
    for k, v in best_cfg.items():
        print(f"  {k}: {v}")

    payload = {
        "source": "05_tune_dnn.py",
        "cv": CV,
        "n_configs": len(configs),
        "max_epochs": MAX_EPOCHS,
        "sample_frac": SAMPLE_FRAC,
        "best_cv_gmpca": float(np.exp(-best_ce)),
        "params": {
            "hidden": list(best_cfg["hidden"]),
            "lr": best_cfg["lr"],
            "dropout": list(best_cfg["dropout"]),
            "weight_decay": best_cfg["weight_decay"],
            "batch_size": best_cfg["batch_size"],
        },
        "all_results": [
            {"cv_ce": ce, "cv_gmpca": float(np.exp(-ce)), "cfg": {k: (list(v) if isinstance(v, tuple) else v) for k, v in cfg.items()}}
            for ce, cfg in results
        ],
        "scaled_features": scaled_features,
    }
    out_path = ARTIFACTS / "lpmc_dnn_custom_params.json"
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"\nHiperparámetros propios guardados en: {out_path}")


if __name__ == "__main__":
    main()
