import shap
import joblib
import pandas as pd

from src.feature_extraction.feature_pipeline import extract_features

model=joblib.load("random_forest_phishing.pkl")

explainer=shap.TreeExplainer(model)

def explain_url(url):

    features=extract_features(url)
    X=pd.DataFrame([features])
    X=X[model.feature_names_in_]
    shap_values=explainer(X)
    
    return shap_values,X,explainer

