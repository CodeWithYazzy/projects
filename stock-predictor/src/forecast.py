import pandas as pd, numpy as np
from sklearn.linear_model import LinearRegression
rng=np.random.default_rng(0)
dates=pd.date_range("2022-01-01", periods=120)
price=100 + np.cumsum(rng.normal(0,1,120)) + np.linspace(0,10,120)
df=pd.DataFrame({"date":dates,"price":price})
df["prev"]=df["price"].shift(1)
df=df.dropna()
X=df[["prev"]]; y=df["price"]
split=100
m=LinearRegression().fit(X[:split], y[:split])
pred=m.predict(X[split:])
print(f"Next pred {pred[-1]:.2f} — baseline trend")
