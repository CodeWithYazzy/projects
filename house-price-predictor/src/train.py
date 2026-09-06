import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
rng = np.random.default_rng(0)
n=200
df=pd.DataFrame({
    "area": rng.integers(500,2500,n),
    "bedrooms": rng.integers(1,5,n),
    "age": rng.integers(0,30,n),
    "location": rng.choice(["A","B","C"], n)
})
df["price"] = df["area"]*300 + df["bedrooms"]*50000 - df["age"]*1000 + rng.normal(0,20000,n) + (df["location"]=="A")*40000
X=df.drop(columns=["price"]); y=df["price"]
pre=ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"), ["location"])], remainder="passthrough")
pipe=Pipeline([("pre",pre),("rf",RandomForestRegressor(n_estimators=50, random_state=0))])
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=0)
pipe.fit(Xtr,ytr)
pred=pipe.predict(Xte)
print(f"RMSE {mean_squared_error(yte,pred)**0.5:.0f}, R2 {r2_score(yte,pred):.3f}")
