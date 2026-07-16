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

        if result['prediction']=='Phishing':
            st.error(
                f"⚠️ {result['prediction']}"
            )
        else:
            st.success(f"✅ {result['prediction']}")

        st.write(
            f"Confidence:{result['confidence']:.2%}"
        )

        st.subheader("Extracted Features")
        feature_df=pd.DataFrame(
            result['features'].items(),
            columns=['Feature','Value']
        )
        st.dataframe(feature_df,use_container_width=True)
        
        st.subheader("Why did the model make this decision?")
        explainer,shap_values,X=explain_url(url)

        fig,ax=plt.subplots()
        st.write(type(shap_values))
        st.write(shap_values.shape)
        st.write(type(shap_values.values))
        st.write(shap_values.values.shape)
        # shap.plots.waterfall(
        #     shap_values[0,:,1],
        #     show=False
        #     )
        # st.pyplot(
        #     plt.gcf()
        # )
        
        # plt.clf()
        

    else:
        st.warning("Please enter a URL.")
    
    

