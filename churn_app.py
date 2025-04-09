import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model, scaler and feature columns
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("Customer Churn Prediction")

# Input Form
def user_input_features():
    data = {
        'gender': st.selectbox('Gender', ['Female', 'Male']),
        'SeniorCitizen': st.selectbox('Senior Citizen', [0, 1]),
        'Partner': st.selectbox('Partner', ['Yes', 'No']),
        'Dependents': st.selectbox('Dependents', ['Yes', 'No']),
        'tenure': st.slider('Tenure (Months)', 0, 72, 12),
        'PhoneService': st.selectbox('Phone Service', ['Yes', 'No']),
        'MultipleLines': st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service']),
        'InternetService': st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No']),
        'OnlineSecurity': st.selectbox('Online Security', ['Yes', 'No', 'No internet service']),
        'OnlineBackup': st.selectbox('Online Backup', ['Yes', 'No', 'No internet service']),
        'DeviceProtection': st.selectbox('Device Protection', ['Yes', 'No', 'No internet service']),
        'TechSupport': st.selectbox('Tech Support', ['Yes', 'No', 'No internet service']),
        'StreamingTV': st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service']),
        'StreamingMovies': st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service']),
        'Contract': st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year']),
        'PaperlessBilling': st.selectbox('Paperless Billing', ['Yes', 'No']),
        'PaymentMethod': st.selectbox('Payment Method', ['Electronic check', 'Mailed check',
                                                          'Bank transfer (automatic)', 'Credit card (automatic)']),
        'MonthlyCharges': st.number_input('Monthly Charges', 0.0, 200.0, 50.0),
        'TotalCharges': st.number_input('Total Charges', 0.0, 10000.0, 1000.0)
    }

    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# One-hot encode user input
input_encoded = pd.get_dummies(input_df)

# Align columns with training features
input_aligned = input_encoded.reindex(columns=feature_columns, fill_value=0)

# Scale
input_scaled = scaler.transform(input_aligned)

# Predict
prediction = model.predict(input_scaled)[0]
probability = model.predict_proba(input_scaled)[0][1]

# Output
st.subheader("Prediction")
st.write("Customer is likely to **Churn**" if prediction == 1 else "Customer is **Not likely** to churn")
st.write(f"Confidence: **{probability*100:.2f}%**")
