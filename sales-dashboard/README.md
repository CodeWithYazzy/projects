# Sales Data Dashboard — Pandas + Matplotlib

> Daily trends and category aggregation — reproducible, no external CSV.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557c)

## Problem
Surface sales trends for operational decisions from 90 days of synthetic transactions.

## Dataset
Synthetic — 90 rows, `date` + `category` (Electronics/Apparel/Grocery) + `amount` (normal + trend), seeded `rng(0)`, 2023-01-01 onwards.

## Approach
`pandas groupby` daily + by category, then `matplotlib` line plot — deterministic.

## Results
`results/daily.png` (10×4, 150dpi) + printed `by_cat` sums — see console.

## Structure
```
sales-dashboard/
├── README.md
├── requirements.txt
├── src/analysis.py
└── results/daily.png (generated)
```

## Quick start
```bash
pip install -r requirements.txt
python src/analysis.py
# open results/daily.png
```

## YasirLab
Part of [yasirlab.in](https://yasirlab.in) Projects — EDA track.
