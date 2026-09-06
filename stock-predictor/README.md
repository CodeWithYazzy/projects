# Stock Price Predictor — Time-Series Baseline

> Windowing, linear baseline, trend eval.

![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458)

## Problem
Forecast next price from history.

## Approach
`date 2022-01-01 +120` → `price = 100 + cumsum(N(0,1)) + trend` → `prev = shift(1)` → `LinearRegression` on first 100 → predict last 20.

## Quick start
```bash
pip install -r requirements.txt
python src/forecast.py
```

## YasirLab
Time-series prototype — next add windowing + ARIMA.
