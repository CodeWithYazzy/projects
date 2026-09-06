# Numpy Data Explorer — Filtering & Grouping

> Fast programmatic exploration of tabular data.

![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243)

## Problem
Enable fast exploration of 100×4 synthetic features.

## Approach
`rng.normal(0,1,(100,4))` → `describe()` + `corr()` + `groupby(f1>0)["f2"].mean()`.

## Quick start
```bash
pip install -r requirements.txt
python src/explorer.py
```

## Structure
```
numpy-explorer/src/explorer.py
```

## YasirLab
Data track — EDA before modeling.
