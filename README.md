
# 📈 Customer Churn Prediction

## 🔍 Overview
Customer churn — when customers stop using a service — is a major concern for subscription-based businesses. This project uses machine learning to predict whether a customer is likely to churn, enabling businesses to take proactive measures and improve retention.

This project includes:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Model training with Random Forest
- Streamlit dashboard for real-time predictions

---

## 📊 Dataset

This project uses the **Telco Customer Churn Dataset** provided by [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

- **Source**: © Original Authors on Kaggle  
- **License**: [Kaggle Terms of Use](https://www.kaggle.com/terms)  
- **Link**: [Telco Customer Churn Dataset on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

> *Note: This dataset is used strictly for educational and non-commercial purposes.*

---

## 🧠 Technologies Used

- Python  
- pandas, NumPy  
- scikit-learn  
- matplotlib, seaborn  
- Streamlit (for UI/dashboard)  
- Jupyter Notebook  

---

## 🗂️ Project Structure

```
customer-churn-prediction/
├── churn_app/                 # Streamlit app
├── dataset/                   # Raw CSV file
├── notebooks/                 # EDA and training notebooks
├── models/                    # Saved model files
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer-churn-prediction.git
   cd customer-churn-prediction
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the Streamlit app:
   ```bash
   streamlit run churn_app/churn_dashboard.py
   ```

---

## 🚀 Results

- **Model Used**: Random Forest Classifier  
- **Accuracy**: ~85% on test data  
- **Key Features**:  
  - Tenure  
  - Monthly Charges  
  - Contract Type  
  - Internet Service  

---

## 📌 How to Use

Once the Streamlit dashboard is launched, users can:
- Input customer data manually
- Predict churn probability instantly
- Visualize churn-related features and trends

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 💼 Connect with Me

If you found this project interesting or useful, feel free to connect on www.linkedin.com/in/ruhmah-leya-47037a2b9


