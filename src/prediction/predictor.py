# src/prediction/predictor.py
import os
import joblib
import pandas as pd

from src.feature_extraction.feature_pipeline import extract_features

MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "models", "random_forest_phishing.pkl"
)
model = joblib.load(MODEL_PATH)

def predict_url(url):
    features = extract_features(url)
    X = pd.DataFrame([features])
    X = X[model.feature_names_in_]
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0]

    return {
        "prediction": "Phishing" if prediction == 1 else "Legitimate",
        "confidence": float(max(probability)),
        "features": features,
    }