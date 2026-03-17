#!/usr/bin/env python

from pathlib import Path
import pandas as pd

pd.set_option("display.max_columns", 150)

ROOT = Path(__file__).resolve().parent
RAW_PATH = ROOT / "data" / "raw" / "LPMC_dataset.csv"
OUT_DIR = ROOT / "data" / "preprocessed"
PROCESSED_PATH = ROOT / "data" / "processed" / "LPMC_processed.csv"
OUT_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    print(f"Leyendo dataset bruto desde: {RAW_PATH}")
    df = pd.read_csv(RAW_PATH)

    print("Forma inicial:", df.shape)

    # Transformaciones categoricas
    purpose_df = pd.get_dummies(df["purpose"], prefix="purpose")
    df = df.join(purpose_df)
    df = df.drop(columns=["purpose"])

    # El profesor no usa faretype en el modelo; se elimina
    df = df.drop(columns=["faretype"])

    fuel_map = {
        "Petrol_Car": "Petrol",
        "Petrol_LGV": "Petrol",
        "Diesel_Car": "Diesel",
        "Diesel_LGV": "Diesel",
        "Hybrid_Car": "Hybrid",
        "Average_Car": "Average",
    }
    df["fueltype"] = df["fueltype"].map(fuel_map)

    fueltype_df = pd.get_dummies(df["fueltype"], prefix="fueltype")
    df = df.join(fueltype_df)
    df = df.drop(columns=["fueltype"])

    mode_map = {"walk": 0, "cycle": 1, "pt": 2, "drive": 3}
    df["travel_mode"] = df["travel_mode"].map(mode_map)

    cols_to_drop = [
        "trip_id",
        "person_n",
        "trip_n",
        "travel_year",
        "travel_month",
        "travel_date",
        "bus_scale",
        "dur_pt_total",
        "dur_pt_int_total",
        "cost_driving_fuel",
        "cost_driving_con_charge",
        "driving_traffic_percent",
    ]
    df = df.drop(columns=cols_to_drop)

    print("Forma tras transformar:", df.shape)

    df.to_csv(PROCESSED_PATH, index=False)

    train_df = df[df["survey_year"].isin([1, 2])].copy()
    test_df = df[df["survey_year"] == 3].copy()

    train_df = train_df.drop(columns=["survey_year"])
    test_df = test_df.drop(columns=["survey_year"])

    print(f"Length of train: {train_df.shape[0]}")
    print(f"Length of test : {test_df.shape[0]}")

    train_path = OUT_DIR / "LPMC_train.csv"
    test_path = OUT_DIR / "LPMC_test.csv"

    train_df.to_csv(train_path, sep=",", index=False)
    test_df.to_csv(test_path, sep=",", index=False)

    print(f"Train guardado en: {train_path}")
    print(f"Test  guardado en: {test_path}")
    print("N columnas finales (features + target):", len(train_df.columns))


if __name__ == "__main__":
    main()
