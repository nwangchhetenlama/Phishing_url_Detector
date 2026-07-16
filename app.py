import streamlit as st 
from src.prediction.predictor import predict_url

st.title("Phishing URL Detector")
url=st.text_input("Enter URL:")

if st.button("Analyze"):

    if url:
        result=predict_url(url)

        if result['prediction']=='Phishing':
            st.error(
                f"⚠️ {result['prediction']}"
            )
        else:
            st.success(f"✅ {result['prediction']}")

        st.write(
            f"Confidence:{result['confidence']:.2%}"
        )

