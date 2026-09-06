# Handwritten Digit Classifier — MNIST CNN

> 28×28 grayscale, Conv blocks, held-out eval.

![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C)

## Problem
Recognize 0–9 digits.

## Architecture
`DigitCNN`: Conv(1→32) → ReLU → MaxPool → Conv(32→64) → ReLU → MaxPool → Flatten → FC(64*7*7→128) → ReLU → FC(10)

## Quick start
```python
from src.model import DigitCNN
m = DigitCNN()
print(m)
```

## YasirLab
Computer Vision — companion to `pytorch-image-classifier`.
