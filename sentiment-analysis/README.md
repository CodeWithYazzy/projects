# Sentiment Analysis Tool — TF-IDF + LogisticRegression

> Text preprocessing, held-out precision/recall.

![NLP](https://img.shields.io/badge/NLP-TF--IDF-blue)

## Problem
Positive/negative sentiment from short reviews.

## Dataset
Synthetic 120 texts (repeat of 6 templates ×20), balanced 1/0, `train_test_split(0.2, stratify)`.

## Approach
`lower → tokenize → stop_words=english → TfidfVectorizer` fit on train only → `LogisticRegression` → held-out report.

## Results
`python src/train.py` prints classification_report (precision/recall/F1 ~1.0 on synthetic).

## Structure
```
sentiment-analysis/
├── src/train.py
└── requirements.txt
```

## Limitation
Bag-of-words — no embeddings yet.

## YasirLab
NLP track — next is transformer fine-tuning.
