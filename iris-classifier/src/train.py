"""Train + cross-validate + save pipeline — reproduces flagship 97% result."""

import json
import pathlib
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

from dataset import get_splits
from model import make_logistic_pipeline, make_rf_pipeline

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
RESULTS = ROOT / "results"
MODELS.mkdir(exist_ok=True)
RESULTS.mkdir(exist_ok=True)

def main():
    (X_train, X_test, y_train, y_test), data = get_splits()

    pipe_lr = make_logistic_pipeline()
    pipe_rf = make_rf_pipeline()

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    cv_lr = cross_val_score(pipe_lr, X_train, y_train, cv=cv)
    cv_rf = cross_val_score(pipe_rf, X_train, y_train, cv=cv)

    print(f"5-fold CV (train 120) — LR: {cv_lr.mean():.4f} ± {cv_lr.std():.4f}")
    print(f"5-fold CV (train 120) — RF: {cv_rf.mean():.4f} ± {cv_rf.std():.4f}")

    # Fit primary on train, evaluate on held-out test (locked)
    pipe_lr.fit(X_train, y_train)
    y_pred = pipe_lr.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\nHeld-out test (30) — LR accuracy: {acc:.4f} ({int(acc*30)}/30) ~ {acc*100:.1f}%")
    print(classification_report(y_test, y_pred, target_names=data.target_names))
    print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

    # Also fit RF for comparison
    pipe_rf.fit(X_train, y_train)
    acc_rf = accuracy_score(y_test, pipe_rf.predict(X_test))
    print(f"Held-out test — RF accuracy: {acc_rf:.4f}")

    # Save primary
    joblib.dump(pipe_lr, MODELS / "iris_pipeline.joblib")
    print(f"\nSaved {MODELS / 'iris_pipeline.joblib'}")

    # Save metrics
    (RESULTS / "metrics.json").write_text(json.dumps({
        "split": "80/20 stratify random_state=0 — 120 train / 30 test",
        "cv_lr_mean": float(cv_lr.mean()),
        "cv_lr_std": float(cv_lr.std()),
        "cv_rf_mean": float(cv_rf.mean()),
        "cv_rf_std": float(cv_rf.std()),
        "heldout_lr_accuracy": float(acc),
        "heldout_rf_accuracy": float(acc_rf),
        "note": "96.67% rounds to 97% in docs"
    }, indent=2))
    (RESULTS / "classification_report.txt").write_text(classification_report(y_test, y_pred, target_names=data.target_names))
    (RESULTS / "confusion_matrix.txt").write_text(str(confusion_matrix(y_test, y_pred)))
    print(f"Saved metrics to {RESULTS}")

if __name__ == "__main__":
    main()
