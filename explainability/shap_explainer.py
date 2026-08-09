
import pandas as pd

from src.feature_extraction.feature_pipeline import extract_features
from pathlib import Path
import joblib
import shap

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "random_forest_phishing.pkl"

model = joblib.load(MODEL_PATH)

explainer = shap.TreeExplainer(model)

def explain_url(url):

    features=extract_features(url)
    X=pd.DataFrame([features])
    X=X[model.feature_names_in_]
    shap_values=explainer(X)

    
    return shap_values,X,explainer

