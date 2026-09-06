from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
X,y=load_breast_cancer(return_X_y=True)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=0,stratify=y)
pipe=Pipeline([("scaler",StandardScaler()),("clf",RandomForestClassifier(random_state=0))])
pipe.fit(Xtr,ytr)
print(classification_report(yte, pipe.predict(Xte)))
