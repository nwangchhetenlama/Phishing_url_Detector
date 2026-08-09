
import joblib
import pickle
import pandas as pd
from pathlib import Path

from src.feature_extraction.feature_pipeline import extract_features


# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

# -------------------------
# Load models
# -------------------------

# Random Forest
RF_MODEL_PATH = BASE_DIR / "models" / "random_forest_phishing.pkl"
rf_model = joblib.load(RF_MODEL_PATH)

# Logistic Regression
LR_MODEL_PATH = BASE_DIR / "models" / "pipe_lr.pkl"
with open(LR_MODEL_PATH, "rb") as f:
    lr_model = pickle.load(f)

# KNN
KNN_MODEL_PATH = BASE_DIR / "models" / "pipe_knn.pkl"
with open(KNN_MODEL_PATH, "rb") as f:
    knn_model = pickle.load(f)


# -------------------------
# Prediction function
# -------------------------

def predict_url(url):

    # Extract features
    features = extract_features(url)

    # Convert features to DataFrame
    X = pd.DataFrame([features])

    # Make sure feature order matches training
    X = X[rf_model.feature_names_in_]

    # -------------------------
    # Random Forest
    # -------------------------

    rf_prediction = rf_model.predict(X)[0]
    rf_probability = rf_model.predict_proba(X)[0]

    # -------------------------
    # Logistic Regression
    # -------------------------

    lr_prediction = lr_model.predict(X)[0]
    lr_probability = lr_model.predict_proba(X)[0]

    # -------------------------
    # KNN
    # -------------------------

    knn_prediction = knn_model.predict(X)[0]
    knn_probability = knn_model.predict_proba(X)[0]

    return {

        "url": url,

        "features": features,

        "random_forest": {
            "prediction": (
                "Phishing" if rf_prediction == 1
                else "Legitimate"
            ),
            "confidence": max(rf_probability)
        },

        "logistic_regression": {
            "prediction": (
                "Phishing" if lr_prediction == 1
                else "Legitimate"
            ),
            "confidence": max(lr_probability)
        },

        "knn": {
            "prediction": (
                "Phishing" if knn_prediction == 1
                else "Legitimate"
            ),
            "confidence": max(knn_probability)
        }
    }

