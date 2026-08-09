
import streamlit as st
from src.prediction.predictor import predict_url
import pandas as pd
import matplotlib.pyplot as plt
import shap
from explainability.shap_explainer import explain_url


if "history" not in st.session_state:
    st.session_state.history = []


st.title("Phishing URL Detector")

url = st.text_input("Enter URL to analyze:")


# -------------------------
# Choose Model
# -------------------------

model_choice = st.selectbox(
    "Choose Model",
    [
        "Random Forest",
        "Logistic Regression",
        "KNN"
    ]
)


if st.button("Analyze"):

    if url:

        result = predict_url(url)

        # -------------------------
        # Select model result
        # -------------------------

        if model_choice == "Random Forest":
            model_result = result["random_forest"]

        elif model_choice == "Logistic Regression":
            model_result = result["logistic_regression"]

        else:
            model_result = result["knn"]


        # -------------------------
        # Prediction History
        # -------------------------

        st.session_state.history.append({
            "url": url,
            "model": model_choice,
            "prediction": model_result["prediction"],
            "confidence": f"{model_result['confidence']:.2%}"
        })


        # -------------------------
        # Analyzed URL
        # -------------------------

        st.subheader("Analyzed URL:")
        st.code(url)


        # -------------------------
        # Prediction
        # -------------------------

        if model_result["prediction"] == "Phishing":

            st.error(
                f"⚠️ {model_result['prediction']}"
            )

        else:

            st.success(
                f"✅ {model_result['prediction']}"
            )


        # -------------------------
        # Confidence + Risk
        # -------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Confidence",
                f"{model_result['confidence']:.2%}"
            )

        with col2:

            st.metric(
                "Risk Level",
                "High"
                if model_result["prediction"] == "Phishing"
                else "Low"
            )


        # -------------------------
        # Extracted Features
        # -------------------------

        st.subheader("Extracted Features")

        feature_df = pd.DataFrame(
            result["features"].items(),
            columns=["Feature", "Value"]
        )

        st.dataframe(
            feature_df,
            use_container_width=True
        )


        # -------------------------
        # SHAP
        # -------------------------

        if model_choice == "Random Forest":

            st.subheader(
                "Why did the model make this decision?"
            )

            shap_values, X, explainer = explain_url(url)

            fig, ax = plt.subplots()

            shap.plots.waterfall(
                shap_values[0, :, 1],
                show=False
            )

            st.pyplot(fig)

            plt.close(fig)


        elif model_choice == "Logistic Regression":

            st.info(
                "SHAP explanation is currently available "
                "for the Random Forest model."
            )


        elif model_choice == "KNN":

            st.info(
                "SHAP explanation is currently available "
                "for the Random Forest model."
            )


    else:

        st.warning("Please enter a URL.")


# -------------------------
# Prediction History
# -------------------------

st.subheader("Prediction History")

if st.session_state.history:

    st.table(
        st.session_state.history
    )

else:

    st.info("No predictions yet.")

