from pathlib import Path
import json
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from recommendation.services.prediction import build_yield_training_bundle


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "crop_model.pkl"
COLUMNS_PATH = BASE_DIR / "columns.pkl"
YIELD_MODEL_PATH = BASE_DIR / "yield_model.pkl"
YIELD_COLUMNS_PATH = BASE_DIR / "yield_columns.pkl"
REQUIRED_COLUMNS = {
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "rainfall",
    "ph",
    "soil_type",
    "label",
}


def find_dataset_path() -> Path:
    preferred_names = [
        "crop_recommendation_dataset.csv",
        "Crop_recommendation_dataset.csv",
        "crop_recommendation_dataset (1).csv",
    ]

    for filename in preferred_names:
        candidate = BASE_DIR / filename
        if candidate.exists():
            return candidate

    for candidate in sorted(BASE_DIR.glob("*.csv")):
        try:
            header = set(pd.read_csv(candidate, nrows=0).columns)
        except Exception:
            continue
        if REQUIRED_COLUMNS.issubset(header):
            return candidate

    raise FileNotFoundError(
        "No matching dataset was found. Make sure a CSV with the required crop columns is in the project folder."
    )


def main() -> None:
    dataset_path = find_dataset_path()
    print(f"Loading dataset from: {dataset_path.name}")

    dataset = pd.read_csv(dataset_path)
    dataset = dataset.dropna(subset=sorted(REQUIRED_COLUMNS))

    features = dataset.drop(columns=["label"])
    features = pd.get_dummies(features, columns=["soil_type"])
    target = dataset["label"].astype(str).str.strip().str.lower()

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
        stratify=target,
    )

    model = RandomForestClassifier(
        n_estimators=220,
        max_depth=18,
        min_samples_leaf=2,
        class_weight="balanced_subsample",
        random_state=42,
        n_jobs=1,
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Accuracy: {accuracy:.4f}")
    print("Classification report:")
    report = classification_report(y_test, predictions, output_dict=True, zero_division=0)
    print(classification_report(y_test, predictions, zero_division=0))

    with MODEL_PATH.open("wb") as model_file:
        pickle.dump(model, model_file)

    with COLUMNS_PATH.open("wb") as columns_file:
        pickle.dump(features.columns.tolist(), columns_file)
    metrics_payload = {
        "accuracy": round(float(accuracy), 6),
        "macro_precision": round(float(report["macro avg"]["precision"]), 6),
        "macro_recall": round(float(report["macro avg"]["recall"]), 6),
        "macro_f1": round(float(report["macro avg"]["f1-score"]), 6),
        "weighted_precision": round(float(report["weighted avg"]["precision"]), 6),
        "weighted_recall": round(float(report["weighted avg"]["recall"]), 6),
        "weighted_f1": round(float(report["weighted avg"]["f1-score"]), 6),
        "training_rows": int(len(dataset)),
        "feature_count": int(features.shape[1]),
        "model": "RandomForestClassifier",
    }
    with (BASE_DIR / "model_metrics.json").open("w", encoding="utf-8") as metrics_file:
        json.dump(metrics_payload, metrics_file, indent=2)

    yield_features, yield_target = build_yield_training_bundle()
    yield_model = RandomForestRegressor(
        n_estimators=180,
        max_depth=16,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=1,
    )
    yield_model.fit(yield_features, yield_target)

    with YIELD_MODEL_PATH.open("wb") as model_file:
        pickle.dump(yield_model, model_file)

    with YIELD_COLUMNS_PATH.open("wb") as columns_file:
        pickle.dump(yield_features.columns.tolist(), columns_file)

    print(f"Saved model to: {MODEL_PATH.name}")
    print(f"Saved feature columns to: {COLUMNS_PATH.name}")
    print("Saved model metrics to: model_metrics.json")
    print(f"Saved yield model to: {YIELD_MODEL_PATH.name}")
    print(f"Saved yield feature columns to: {YIELD_COLUMNS_PATH.name}")


if __name__ == "__main__":
    main()
