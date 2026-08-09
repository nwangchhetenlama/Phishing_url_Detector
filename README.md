# Phishing URL Detector

A machine learning system that detects phishing URLs using URL structure, HTML content, and WHOIS domain data. Includes a Streamlit web app, a FastAPI backend, multiple machine learning models, and SHAP-based explainability.

## Features

* **URL-based features**: length, digit ratio, token count, character repetition, hostname length
* **HTML-based features**: phishing keyword detection, internal/external link ratios, redirect analysis
* **WHOIS-based features**: domain age
* **Machine Learning Models**:

  * Random Forest Classifier
  * Logistic Regression with feature engineering and preprocessing
  * K-Nearest Neighbors (KNN) with preprocessing
* **Model Selection**: Select Random Forest, Logistic Regression, or KNN from the Streamlit interface
* **Model Comparison**: Compare predictions and confidence scores from the available models
* **Explainability**: SHAP waterfall plots for Random Forest predictions
* **Streamlit app**: Interactive UI for single-URL analysis
* **FastAPI backend**: REST API using Random Forest only for programmatic predictions

## Project Structure

```text
├── app.py                          # Streamlit UI
├── src/
│   ├── api/                        # FastAPI backend
│   ├── feature_extraction/         # URL, HTML, WHOIS feature extractors
│   └── prediction/                 # Model loading and prediction logic
├── explainability/                 # SHAP explainer
├── models/
│   ├── random_forest_phishing.pkl  # Random Forest model
│   ├── pipe_lr.pkl                 # Logistic Regression pipeline
│   └── pipe_knn.pkl                # KNN pipeline
├── data/                           # Raw and processed datasets
├── notebooks/                      # EDA and model training notebooks
└── requirements.txt
```

## Machine Learning Models

### Random Forest

Random Forest is the primary model used in the project.

It is used for:

* Streamlit predictions
* SHAP explainability
* FastAPI `/predict` endpoint

### Logistic Regression

Logistic Regression is implemented with feature preprocessing and regularization.

The preprocessing pipeline includes:

```text
Missing Value Handling
        ↓
SimpleImputer
        ↓
StandardScaler
        ↓
Logistic Regression
```

The fitted pipeline is saved as:

```text
models/pipe_lr.pkl
```

Logistic Regression is available for prediction and model comparison in the Streamlit application.

### K-Nearest Neighbors (KNN)

KNN is implemented using a preprocessing pipeline with feature scaling.

The fitted pipeline is saved as:

```text
models/pipe_knn.pkl
```

KNN is available for prediction and model comparison in the Streamlit application.

## Model Selection

The Streamlit application allows the user to choose between:

* Random Forest
* Logistic Regression
* KNN

The selected model provides:

* Prediction
* Confidence score
* Risk level

This allows the performance and predictions of different machine learning approaches to be compared on the same URL.

## Explainability

SHAP is currently used to explain the **Random Forest model**.

The application generates a SHAP waterfall plot showing how individual features contributed to the prediction.

```text
URL
 ↓
Feature Extraction
 ↓
Random Forest
 ↓
Prediction
 ↓
SHAP
 ↓
Feature Contributions
```

Logistic Regression and KNN predictions are currently displayed without the Random Forest SHAP waterfall explanation.

## Setup

```bash
git clone <repo-url>
cd Phishing_url_Detector
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Exploratory Data Analysis

* Loaded the phishing dataset into a Pandas DataFrame and inspected row/column counts, data types, missing values, and duplicates.
* Analyzed class distribution, feature value distribution, and correlation between features.
* Identified which features are strong indicators of phishing behavior.
* Performed feature preprocessing for Logistic Regression and KNN.
* Applied feature scaling where required by the models.
* Performed outlier analysis during the feature engineering process.

**Key observations:**

* The dataset contains both legitimate and phishing websites.
* Several URL-based features show strong correlation with phishing behavior.
* Some features can be extracted directly from URLs, while others require HTML content or external services such as WHOIS.

**Feature categories:**

*URL-based* (extracted directly from the URL): URL length, number of dots, number of hyphens, presence of IP address, number of subdomains, presence of special characters.

*HTML-based* (require webpage scraping): external resource ratio, number of links, forms and redirects, favicon source.

*WHOIS-based*: domain age.

## Running the Streamlit App

The deployed Streamlit application is available at:

```text
https://phishingurldetector-nclrdezrccba2cf8dws3pi.streamlit.app/
```

To run the application locally:

```bash
python -m streamlit run app.py
```

The Streamlit application allows users to:

1. Enter a URL
2. Select a machine learning model
3. Analyze the URL
4. View the prediction
5. View confidence
6. View risk level
7. View extracted features
8. View prediction history
9. View SHAP explanation for Random Forest

## Running the FastAPI Backend

The FastAPI backend currently uses **Random Forest only**.

Run:

```bash
python -m uvicorn src.api.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### `/predict` Endpoint

The `/predict` endpoint uses the Random Forest model for programmatic predictions.

**Request body:**

```json
{
    "url": "https://example.com"
}
```

**Example response:**

```json
{
    "prediction": "Legitimate",
    "confidence": 0.98
}
```

> **Note:** Logistic Regression and KNN are currently available in the Streamlit application but are not used by the FastAPI `/predict` endpoint.

## Model Performance

### Random Forest

| Metric    | Score |
| --------- | ----: |
| Accuracy  |  0.92 |
| Precision |  0.90 |
| Recall    |  0.93 |
| F1 Score  |  0.92 |

Logistic Regression and KNN have been added for model comparison. Their final performance scores can be added after evaluating both models on the final test set.

## Contributors

* Nwang Chheten Lama
* Shubham Adhikari
