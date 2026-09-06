"""Dataset loading and splitting — no leakage, reproducible."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

RANDOM_STATE = 0
TEST_SIZE = 0.2

FEATURE_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
TARGET_NAMES = ["setosa", "versicolor", "virginica"]

def load_data():
    data = load_iris()
    X = data.data  # 150 x 4
    y = data.target
    return X, y, data

def get_splits():
    X, y, data = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        stratify=y,
        random_state=RANDOM_STATE,
    )
    return (X_train, X_test, y_train, y_test), data
