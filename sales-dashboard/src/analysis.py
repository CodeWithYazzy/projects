import pandas as pd, numpy as np, matplotlib.pyplot as plt, pathlib
# Generate synthetic sales data (deterministic)
rng = np.random.default_rng(0)
dates = pd.date_range("2023-01-01", periods=90, freq="D")
df = pd.DataFrame({
    "date": dates,
    "category": rng.choice(["Electronics","Apparel","Grocery"], 90),
    "amount": (rng.normal(500, 120, 90).round(2) + np.linspace(0,100,90)).clip(100)
})
pathlib.Path("results").mkdir(exist_ok=True)
# Aggregate
daily = df.groupby("date")["amount"].sum()
by_cat = df.groupby("category")["amount"].sum()
print(daily.head())
print(by_cat)
# Plot
plt.figure(figsize=(10,4))
daily.plot()
plt.title("Daily Sales — 90 days")
plt.tight_layout()
plt.savefig("results/daily.png", dpi=150)
print("Saved results/daily.png")
