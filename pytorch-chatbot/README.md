# PyTorch Chatbot — Seq Model Stub

> Tokenization + GRU training loop scaffold.

![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C)

## Problem
Generate coherent response to short prompt.

## Approach
`vocab={hello:0...}` → `Embedding(4,8) → GRU(8,16) → Linear(16,4)` → shape `2×4` verified.

## Quick start
```bash
pip install -r requirements.txt
python src/chatbot.py
```

## Next
Add dialogue corpus + cross-entropy training.

## YasirLab
NLP/Deep Learning — see also sentiment.
