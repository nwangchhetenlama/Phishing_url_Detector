from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.prediction.predictor import predict_url

app = FastAPI(title="Phishing URL Detector API")


class URLRequest(BaseModel):
    url: str


class PredictionResponse(BaseModel):
    url: str
    prediction: str
    confidence: float
    features: dict


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: URLRequest):
    try:
        result = predict_url(request.url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not analyze URL: {e}")

    return {
        "url": request.url,
        "prediction": result["prediction"],
        "confidence": result["confidence"],
        "features": result["features"],
    }