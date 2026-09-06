# Calculator App — Desktop + Browser

> Tkinter desktop app with browser localDemo fallback.

![Python](https://img.shields.io/badge/Python-Tkinter-3776AB)

## Problem
Evaluate arithmetic with correct precedence and history.

## Structure
```
calculator-app/
├── README.md
├── app.py      # stub — real app at ../calculator-app.py (Tkinter)
└── requirements.txt (none)
```
Root `calculator-app.py` is the runnable desktop app:

```bash
python calculator-app.py
```

## Browser
`yasirlab.in` runs same logic via safe `evaluateLocally()` (no `eval`) + optional `server.py` backend.

## YasirLab
Utility track — `localDemo: calculator` on the portfolio.
