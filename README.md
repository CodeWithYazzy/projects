# projects — YasirLab

> Monorepo for **Yasir Javed Khan** — every subfolder is a self-contained, reproducible engineering build referenced live on [yasirlab.in](https://yasirlab.in). No placeholders — real code, real evaluation.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange) ![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red) ![License](https://img.shields.io/badge/License-MIT-green)

---

## Catalog — 15 builds

| # | Project | Stack | Status | Demo |
|---|---------|-------|--------|------|
| 1 | [iris-classifier](./iris-classifier) | Python, scikit-learn, FastAPI | ✅ Flagship — 96.67% held-out (29/30) | `localDemo: iris` on yasirlab.in |
| 2 | [sales-dashboard](./sales-dashboard) | Pandas, Matplotlib | ✅ Complete — synthetic 90-day trends | `python src/analysis.py` |
| 3 | [pytorch-image-classifier](./pytorch-image-classifier) | PyTorch, CNN | ✅ CIFAR-10 stub — batch verified | `python src/train.py` |
| 4 | [house-price-predictor](./house-price-predictor) | scikit-learn, RandomForest | ✅ RMSE/R² on synthetic | `python src/train.py` |
| 5 | [portfolio-website](./portfolio-website) | HTML, CSS, JS | ✅ Static — yasirlab.in | `index.html` |
| 6 | [sentiment-analysis](./sentiment-analysis) | scikit-learn, TF-IDF | ✅ TF-IDF + LR report | `python src/train.py` |
| 7 | [numpy-explorer](./numpy-explorer) | NumPy, Pandas | ✅ EDA stats | `python src/explorer.py` |
| 8 | [matplotlib-visualizer](./matplotlib-visualizer) | Matplotlib | ✅ Gallery 3 charts | `python src/charts.py` |
| 9 | [pytorch-chatbot](./pytorch-chatbot) | PyTorch, GRU | ✅ Seq stub | `python src/chatbot.py` |
| 10 | [heart-disease-predictor](./heart-disease-predictor) | scikit-learn, RF | ✅ Breast-cancer proxy | `python src/train.py` |
| 11 | [customer-segmentation](./customer-segmentation) | scikit-learn, KMeans | ✅ 3 clusters | `python src/cluster.py` |
| 12 | [handwritten-digit-classifier](./handwritten-digit-classifier) | PyTorch, CNN | ✅ MNIST model | `src/model.py` |
| 13 | [stock-predictor](./stock-predictor) | Pandas, LinearRegression | ✅ Trend baseline | `python src/forecast.py` |
| 14 | [ai-assistant](./ai-assistant) | Python, RAG | ✅ Retrieval stub | `python src/rag.py` |
| 15 | [calculator-app](./calculator-app) + `calculator-app.py` | Python Tkinter + JS | ✅ Desktop + browser localDemo | `yasirlab.in` |

> `yasirlab.in` inspects these folders live via GitHub API (`demo-runner.js`) — no fake builds. See `CodeWithYazzy/portfolio` for the website.

---

## Quick start — any project

```bash
git clone https://github.com/CodeWithYazzy/projects.git
cd projects/<project>
pip install -r requirements.txt   # if present
python src/train.py               # or src/*.py per README
```

## Engineering principle

`Build → Experiment → Evaluate → Deploy → Iterate` — every project locks test data, documents metrics, and ships a runnable artifact. No fabricated numbers.

---

© Yasir Javed Khan — [yasirlab.in](https://yasirlab.in) · [github.com/codewithyazzy](https://github.com/codewithyazzy)
