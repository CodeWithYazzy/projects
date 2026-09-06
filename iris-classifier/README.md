# Iris Flower Classifier — End-to-end Tabular Pipeline

> **Flagship project for YasirLab** — a complete classification system from raw measurements to deployed inference. Built to demonstrate rigorous ML engineering, not a notebook-only demo.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange) ![License](https://img.shields.io/badge/License-MIT-green)

---

## Problem

Classify iris species (*setosa / versicolor / virginica*) from 4 numeric measurements — sepal length, sepal width, petal length, petal width.

## Dataset

- **Source:** `sklearn.datasets.load_iris` — 150 samples, 4 numeric features, 3 balanced classes (50 each)
- **Split:** 80/20 stratified — `train_test_split(..., test_size=0.2, stratify=y, random_state=0)`
- **Train:** 120 samples (40 per class) | **Test (held-out):** 30 samples (10 per class)
- **Preprocessing:** `StandardScaler` — fit **on train only**, applied to test

> No external CSV needed. Dataset is embedded in scikit-learn and loaded reproducibly.

## Architecture

Single-stage scikit-learn pipeline:

```
StandardScaler → LogisticRegression(max_iter=200)   [primary]
StandardScaler → RandomForestClassifier(n_estimators=100)  [baseline]
```

Both pipelines are compared via **5-fold stratified cross-validation** on train, then final model evaluated on locked held-out test.

## Results — Held-out Test (honest, no leakage)

Run `python src/train.py` to reproduce — metrics are computed at runtime, not hardcoded.

- **Primary (Logistic Regression):** **96.67% accuracy (29/30)** → rounded to **97%** in docs
- **Baseline (Random Forest):** 100% on this split (seed 0) — see `results/metrics.json`
- Cross-validated mean (5-fold on train): ~96% ± 2% — logged by `train.py`

Confusion matrix and classification report are written to `results/` — see `results/confusion_matrix.txt` and `results/classification_report.txt`.

> Versicolor/Virginica overlap explains the single error — consistent with petal dimension overlap noted in Error Analysis.

## Project Structure

```
iris-classifier/
├── README.md
├── requirements.txt
├── app.py                 # FastAPI inference (optional)
├── src/
│   ├── dataset.py         # load + split logic
│   ├── model.py           # pipeline factory
│   ├── train.py           # cross-val + fit + save
│   ├── evaluate.py        # held-out evaluation
│   └── predict.py         # single-row predict API
├── notebooks/
│   └── eda.ipynb          # exploratory (optional)
└── results/               # generated after training (gitignored except sample)
```

## Quick Start

```bash
pip install -r requirements.txt
python src/train.py        # trains, cross-validates, saves models/iris_pipeline.joblib + results/
python src/evaluate.py     # prints held-out metrics + confusion matrix
python -c "from src.predict import predict; print(predict([5.1,3.5,1.4,0.2]))"
```

### API

```bash
pip install fastapi uvicorn
uvicorn app:app --reload
# POST /predict  {"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}
```

## Engineering Notes

- **Reproducible:** fixed seeds (`random_state=0`), pipeline serialization via `joblib`
- **No leakage:** scaler fit on train only, test locked until final evaluation
- **Evaluation:** accuracy, per-class precision/recall/F1, confusion matrix
- **Limitations:** small, clean dataset — not noisy production data; no drift handling yet; petal overlap caps ceiling
- **Deployment:** `predict()` loads `models/iris_pipeline.joblib` and handles single-row inference

## YasirLab Flagship Context

This project is the **most detailed** case study on [yasirlab.in](https://yasirlab.in/#flagship) — see *Experiments* (LR vs RF, scaling ablation, 5-fold vs single split) and *Error Analysis* there.

---

© Yasir Javed Khan — Build → Experiment → Evaluate → Deploy → Iterate
