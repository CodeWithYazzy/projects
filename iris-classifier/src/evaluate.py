"""Held-out evaluation — loads saved pipeline, prints honest metrics."""

import pathlib
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from dataset import get_splits

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "iris_pipeline.joblib"

def main():
    if not MODEL_PATH.exists():
        print(f"Model not found at {MODEL_PATH} — run python src/train.py first")
        return
    pipe = joblib.load(MODEL_PATH)
    (X_train, X_test, y_train, y_test), data = get_splits()
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Held-out accuracy: {acc:.4f} ({acc*100:.2f}%)")
    print(classification_report(y_test, y_pred, target_names=data.target_names))
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    main()
