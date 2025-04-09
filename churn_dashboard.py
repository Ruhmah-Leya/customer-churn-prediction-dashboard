import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

# Function to preprocess input
def preprocess_input(data, feature_columns):
    # Encode categorical variables
    data_encoded = pd.get_dummies(data)
    
    # Align input features with training data
    data_encoded = data_encoded.reindex(columns=feature_columns, fill_value=0)
    
    # Scale features
    scaled = scaler.transform(data_encoded)
    return scaled

# Title
st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("Predict whether a customer will churn based on their service usage and contract information.")

# Sidebar input form
st.sidebar.header("Input Customer Details")
def user_input_features():
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
    Partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
    Dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
    PhoneService = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.sidebar.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.sidebar.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.sidebar.selectbox("Payment Method", [
        "Electronic check", "Mailed check", 
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    MonthlyCharges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=50.0)
    TotalCharges = st.sidebar.number_input("Total Charges", min_value=0.0, value=100.0)

    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }

    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Load feature columns from training
feature_columns = joblib.load("feature_columns.pkl")  # Save this during training!

# Preprocess input
input_scaled = preprocess_input(input_df, feature_columns)

# Predict
prediction = model.predict(input_scaled)[0]
prob = model.predict_proba(input_scaled)[0][1]

# Display results
st.subheader("Prediction Result")
st.write("Churn Probability: {:.2f}%".format(prob * 100))

if prediction == 1:
    st.error("⚠️ The customer is likely to churn.")
else:
    st.success("✅ The customer is likely to stay.")
