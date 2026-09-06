# House Price Predictor — Tabular Regression

> Feature engineering + RandomForest, 80/20 split, RMSE/R².

![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange)

## Problem
Estimate house price from area, bedrooms, age, location.

## Dataset
Synthetic 200 rows — `area` 500–2500, `bedrooms` 1–4, `age` 0–30, `location` A/B/C, price = 300*area + 50000*bedrooms -1000*age + location premium + noise.

## Approach
`ColumnTransformer` OneHot location + passthrough numeric → `RandomForestRegressor(50)` → `train_test_split(0.2)`.

## Results
`python src/train.py` prints e.g. `RMSE ~21000, R² ~0.97` (seed 0).

## Structure
```
house-price-predictor/
├── src/train.py
└── requirements.txt
```

## Quick start
```bash
pip install -r requirements.txt
python src/train.py
```

## Limitation
Synthetic — real market drift needs retraining.

## YasirLab
Tabular ML track — flagship is `iris-classifier`.
