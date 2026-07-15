import joblib
import pandas as pd
import sys
import os

sys.path.append(
    os.path.abspath("..")
)

from src.feature_extraction.feature_pipeline import extract_features

model=joblib.load('./random_forest_phishing.pkl')

def predict_url(url):
    features=extract_features(url)

    X=pd.DataFrame([features])
    X=X[model.feature_names_in_]
    prediction=model.predict(X)[0]
    probability=model.predict_proba(X)[0]
    
    return {
        "prediction":"Phishing" if prediction==1 else "Legitimate",
        "confidence":max(probability)
    }
