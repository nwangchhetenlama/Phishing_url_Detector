import streamlit as st 
from src.prediction.predictor import predict_url
import pandas as pd
import matplotlib.pyplot as plt
import shap
from explainability.shap_explainer import explain_url

st.title("Phishing URL Detector")
url=st.text_input("Enter URL to analyze:")

if st.button("Analyze"):

    if url:

        result=predict_url(url)
        st.subheader("Analyzed URL:")
        st.code(url)

        

        if result['prediction']=='Phishing':
            st.error(
                f"⚠️ {result['prediction']}"
            )
        else:
            st.success(f"✅ {result['prediction']}")

        col1,col2=st.columns(2)
        with col1:
            st.metric(
                "Confidence",f"{result['confidence']:.2%}"
            )
        with col2:
            st.metric(
                "Risk Level",
                "High" if result['prediction']=='Phishing' else "Low"
            )

        st.subheader("Extracted Features")
        feature_df=pd.DataFrame(
            result['features'].items(),
            columns=['Feature','Value']
        )
        st.dataframe(feature_df,use_container_width=True)
        
        st.subheader("Why did the model make this decision?")
        shap_values,X,explainer=explain_url(url)

        fig,ax=plt.subplots()

        shap.plots.waterfall(
            shap_values[0,:,1],
            show=False
            )
        st.pyplot(
            plt.gcf()
        )
        
        plt.clf()
        

    else:
        st.warning("Please enter a URL.")
    
    

