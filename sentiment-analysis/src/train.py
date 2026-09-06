from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
texts = ["I love this product","Terrible service","Great value, will buy again","Worst experience ever","Absolutely fantastic!","Not good, not bad"]*20
y = [1,0,1,0,1,0]*20
Xtr,Xte,ytr,yte=train_test_split(texts,y,test_size=0.2,random_state=0,stratify=y)
vec=TfidfVectorizer(stop_words="english")
Xtrv=vec.fit_transform(Xtr)
clf=LogisticRegression().fit(Xtrv,ytr)
pred=clf.predict(vec.transform(Xte))
print(classification_report(yte,pred))
