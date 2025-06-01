import streamlit as st


def show_presentation_page():
    st.title("🎓 Predictive Maintenance Project")

    st.markdown("""
    ## Project Overview
    **Goal:** Develop ML model for equipment failure prediction

    ### Key Steps:
    1. Data collection from [UCI Repository](https://archive.ics.uci.edu/dataset/601/predictive+maintenance+dataset)
    2. Data preprocessing and feature engineering
    3. Model training (Random Forest, XGBoost, SVM)
    4. Streamlit application development

    ### Technical Stack:
    - Python 3.10
    - Scikit-learn
    - Streamlit
    - Pandas/Matplotlib

    ## Results
    - Best model: **Random Forest** (95% accuracy)
    - Key failure indicators:
        - High tool wear (>200 min)
        - Low temperature difference (<8.6K)

    ## Next Steps
    1. Hyperparameter tuning
    2. Real-time monitoring integration
    3. Anomaly detection implementation
    """)

    st.image("https://miro.medium.com/v2/resize:fit:1200/1*Qc0D7vV4Y6f5hcaE0b0E4g.png",
             caption="Predictive Maintenance Workflow")