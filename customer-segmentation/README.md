# Customer Segmentation — K-Means

> Scaling + clustering + profiling.

![Clustering](https://img.shields.io/badge/Clustering-KMeans-blue)

## Problem
Segment customers for targeted analysis.

## Dataset
Synthetic 120 — `spend ~ N(500,150)` + `visits ~ Poisson(8)`.

## Approach
`StandardScaler` → `KMeans(3, random_state=0)` → `groupby(cluster).mean()`.

## Quick start
```bash
pip install -r requirements.txt
python src/cluster.py
```

## YasirLab
Unsupervised track.
