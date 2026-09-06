"""FastAPI inference — API-ready wrapper for YasirLab flagship."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.predict import predict, predict_proba

app = FastAPI(title="Iris Classifier — YasirLab", version="1.0.0")

class IrisInput(BaseModel):
    sepal_length: float = Field(..., example=5.1)
    sepal_width: float = Field(..., example=3.5)
    petal_length: float = Field(..., example=1.4)
    petal_width: float = Field(..., example=0.2)

@app.get("/")
def health():
    return {"status": "ok", "model": "iris_pipeline.joblib", "classes": ["setosa","versicolor","virginica"]}

@app.post("/predict")
def predict_one(inp: IrisInput):
    feats = [inp.sepal_length, inp.sepal_width, inp.petal_length, inp.petal_width]
    label = predict(feats)
    proba = predict_proba(feats)[0]
    return {"prediction": label, "probabilities": dict(zip(["setosa","versicolor","virginica"], proba)), "input": feats}
