import matplotlib.pyplot as plt, numpy as np, pathlib
pathlib.Path("results").mkdir(exist_ok=True)
x=np.linspace(0,10,100)
plt.figure(); plt.plot(x, np.sin(x)); plt.title("Line"); plt.savefig("results/line.png", dpi=150)
plt.figure(); plt.bar([1,2,3],[3,5,2]); plt.title("Bar"); plt.savefig("results/bar.png", dpi=150)
plt.figure(); plt.scatter(np.random.randn(50), np.random.randn(50)); plt.title("Scatter"); plt.savefig("results/scatter.png", dpi=150)
print("Saved results/*.png")
