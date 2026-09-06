"""Single-row inference — loads pipeline and predicts."""

import pathlib
import joblib
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "iris_pipeline.joblib"
TARGET_NAMES = ["setosa", "versicolor", "virginica"]

_pipe = None

def _load():
    global _pipe
    if _pipe is None:
        if not MODEL_PATH.exists():
            # fallback: train on the fly if model not yet saved (for demo envs)
            from dataset import get_splits
            from model import make_logistic_pipeline
            (X_train, X_test, y_train, y_test), _ = get_splits()
            p = make_logistic_pipeline()
            p.fit(X_train, y_train)
            _pipe = p
        else:
            _pipe = joblib.load(MODEL_PATH)
    return _pipe

def predict(features):
    """
    features: [sepal_length, sepal_width, petal_length, petal_width] or list of such rows
    returns: class name(s)
    """
    pipe = _load()
    arr = np.asarray(features, dtype=float)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    preds = pipe.predict(arr)
    names = [TARGET_NAMES[int(p)] for p in preds]
    return names[0] if len(names) == 1 else names

def predict_proba(features):
    pipe = _load()
    arr = np.asarray(features, dtype=float)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    return pipe.predict_proba(arr).tolist()
