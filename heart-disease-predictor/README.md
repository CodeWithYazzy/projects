# Heart Disease Predictor — Tabular Classifier

> Missing-value handling, scaling, 80/20 split, RandomForest.

![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange)

## Problem
Heart disease presence from clinical features — demo on breast-cancer dataset (proxy for Cleveland 303, same pipeline).

## Dataset
`load_breast_cancer` 569×30, train 455 / test 114, `StandardScaler` fit on train.

## Results
`python src/train.py` prints classification_report.

## Structure
```
heart-disease-predictor/src/train.py
```

## YasirLab
ML track — same pattern as iris.
