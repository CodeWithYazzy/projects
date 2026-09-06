import numpy as np, pandas as pd
rng=np.random.default_rng(0)
a=rng.normal(0,1,(100,4))
df=pd.DataFrame(a, columns=["f1","f2","f3","f4"])
print(df.describe())
print("\nCorr:\n", df.corr().round(2))
print("\nGrouped mean", df.groupby((df["f1"]>0))["f2"].mean())
