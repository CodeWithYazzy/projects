import numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
rng=np.random.default_rng(0)
df=pd.DataFrame({"spend":rng.normal(500,150,120),"visits":rng.poisson(8,120)})
X=StandardScaler().fit_transform(df)
km=KMeans(n_clusters=3, random_state=0, n_init=10).fit(X)
df["cluster"]=km.labels_
print(df.groupby("cluster").mean().round(1))
