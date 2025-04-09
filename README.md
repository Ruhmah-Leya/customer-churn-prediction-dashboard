

# Customer Churn Prediction

## Description

This project implements a **Customer Churn Prediction** model using machine learning to predict whether a customer will churn (leave) a telecommunications company based on various customer features. The model is trained using a real-world dataset, and the application is built using **Streamlit** to make predictions on new customer data via an interactive dashboard.

## Problem Statement

In a competitive market, retaining customers is vital for any business. Predicting whether a customer will churn or not helps businesses take proactive measures to improve customer satisfaction and reduce churn rates. This project applies machine learning to predict customer churn based on several factors like customer demographics, service usage, and payment details.

## Dataset

The dataset used in this project contains customer information from a telecommunications company and includes the following features:

- **customerID**: Unique identifier for each customer
- **gender**: Gender of the customer (Male/Female)
- **SeniorCitizen**: Whether the customer is a senior citizen (1/0)
- **Partner**: Whether the customer has a partner (Yes/No)
- **Dependents**: Whether the customer has dependents (Yes/No)
- **tenure**: Number of months the customer has been with the company
- **PhoneService**: Whether the customer has phone service (Yes/No)
- **MultipleLines**: Whether the customer has multiple lines (Yes/No/No phone service)
- **InternetService**: Type of internet service the customer has (DSL/Fiber optic/No)
- **OnlineSecurity**: Whether the customer has online security (Yes/No)
- **OnlineBackup**: Whether the customer has online backup (Yes/No)
- **DeviceProtection**: Whether the customer has device protection (Yes/No)
- **TechSupport**: Whether the customer has tech support (Yes/No)
- **StreamingTV**: Whether the customer has streaming TV service (Yes/No)
- **StreamingMovies**: Whether the customer has streaming movies service (Yes/No)
- **Contract**: Type of contract the customer has (Month-to-month/One year/Two year)
- **PaperlessBilling**: Whether the customer has paperless billing (Yes/No)
- **PaymentMethod**: Payment method chosen by the customer (Electronic check/Mailed check/Bank transfer/ Credit card)
- **MonthlyCharges**: Monthly charges the customer incurs
- **TotalCharges**: Total charges the customer has paid

The target variable is the **Churn** column, which indicates whether the customer has churned (`Yes`) or not (`No`).

## Technologies

- **Machine Learning:** scikit-learn, RandomForestClassifier
- **Web App:** Streamlit
- **Data Preprocessing:** pandas, numpy
- **Model Saving:** joblib (to save and load models)
- **Visualization:** matplotlib, seaborn

## Features

- **Interactive Dashboard**: Built with **Streamlit** to allow users to input customer data and get predictions about customer churn.
- **Model Training**: Using **Random Forest Classifier** to predict churn based on historical customer data.
- **Data Preprocessing**: Includes encoding categorical features, handling missing values, and scaling numerical features.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer-churn-prediction.git
    ```

2. Navigate to the project folder:
    ```bash
    cd customer-churn-prediction
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run churn_dashboard.py
    ```

5. The app will open in your default browser. You can input customer details, and the model will predict whether the customer will churn or not.

## How It Works

1. The dataset is loaded, cleaned, and preprocessed.
2. Categorical features are one-hot encoded, and numerical features are scaled for model training.
3. A **RandomForestClassifier** is trained to predict customer churn.
4. The trained model is saved and later used to make predictions on new data provided by the user via the Streamlit app.
5. The prediction is displayed in the dashboard: "Customer will churn" or "Customer will not churn."

## Contributing

Feel free to fork the repository, make changes, and create pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
