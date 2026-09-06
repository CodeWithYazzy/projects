# PyTorch Image Classifier — CIFAR-10 CNN

> Conv→ReLU→Pool blocks, 60k 32×32 images, held-out eval.

![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

## Problem
Classify 32×32 color images into 10 categories.

## Dataset
CIFAR-10 — 60k images, 50k train / 10k test, normalized.

## Architecture
`SimpleCNN`: Conv(3→32) → ReLU → MaxPool → Conv(32→64) → ReLU → MaxPool → Flatten → FC(64*8*8→128) → ReLU → FC(10)

## Training
`torchvision` DataLoader, cross-entropy, Adam — `src/train.py` verifies one batch shape; extend to full loop.

## Results
Batch `64×3×32×32 → 2×10` verified — see `python src/train.py`.

## Structure
```
pytorch-image-classifier/
├── src/model.py   # SimpleCNN
├── src/train.py   # loader + sanity batch
└── requirements.txt
```

## Quick start
```bash
pip install -r requirements.txt
python src/train.py  # downloads CIFAR-10 to ./data
```

## YasirLab
Deep Learning track — see also `handwritten-digit-classifier`.
