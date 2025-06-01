import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score


def show_analysis_page():
    st.title("📊 Predictive Maintenance Analysis")

    # Data loading
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
    else:
        from ucimlrepo import fetch_ucirepo
        dataset = fetch_ucirepo(id=601)
        data = pd.concat([dataset.data.features, dataset.data.targets], axis=1)

    # Preprocessing
    data = data.drop(columns=['UDI', 'Product ID', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF'], errors='ignore')
    data['Type'] = LabelEncoder().fit_transform(data['Type'])

    # EDA
    st.subheader("Data Exploration")
    st.dataframe(data.head())

    fig, ax = plt.subplots()
    sns.countplot(x='Machine failure', data=data, ax=ax)
    st.pyplot(fig)

    # Model training
    X = data.drop('Machine failure', axis=1)
    y = data['Machine failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

    st.subheader("Model Performance")
    col1, col2 = st.columns(2)
    col1.metric("Accuracy", f"{accuracy:.2%}")
    col2.metric("ROC AUC", f"{auc:.2%}")

    # Prediction interface
    st.subheader("Failure Prediction")
    with st.form("prediction_form"):
        type_val = st.selectbox("Equipment Type", ["L", "M", "H"])
        air_temp = st.number_input("Air Temperature (K)", value=300.0)
        process_temp = st.number_input("Process Temperature (K)", value=310.0)
        rotational_speed = st.number_input("Rotational Speed (rpm)", value=1500)
        torque = st.number_input("Torque (Nm)", value=40.0)
        tool_wear = st.number_input("Tool Wear (min)", value=0)

        if st.form_submit_button("Predict"):
            input_data = pd.DataFrame({
                'Type': [type_val],
                'Air temperature [K]': [air_temp],
                'Process temperature [K]': [process_temp],
                'Rotational speed [rpm]': [rotational_speed],
                'Torque [Nm]': [torque],
                'Tool wear [min]': [tool_wear]
            })
            input_data['Type'] = LabelEncoder().fit_transform(input_data['Type'])
            input_data = scaler.transform(input_data)

            proba = model.predict_proba(input_data)[0][1]
            st.success(f"Failure probability: {proba:.1%}")
            if proba > 0.5:
                st.error("⚠️ Maintenance recommended!")
            else:
                st.success("✅ Equipment status normal")