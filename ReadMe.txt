# 🛍️ Product Return Prediction System

## 📌 Project Overview

This project aims to predict whether a product will be returned or not using Machine Learning techniques. The system analyzes customer behavior, product details, and transaction features to estimate return risk.

---

## 🎯 Problem Statement

In e-commerce platforms, product returns lead to significant financial losses.
Our goal is to build a system that predicts **return probability at the time of purchase**, helping businesses take preventive actions.

---

## 🧠 Solution Approach

We developed an end-to-end Machine Learning pipeline:

1. Data Cleaning & Preprocessing
2. Feature Engineering
3. Model Training & Evaluation
4. Deployment using Streamlit

---

## 📊 Dataset Description

The dataset contains:

* Customer details (age, gender, location)
* Product details (price, category)
* Transaction details (quantity, discount, time)
* Target variable: `Return_Status` (0 = Not Returned, 1 = Returned)

---

## ⚙️ Data Preprocessing

* Handled missing values using mean/mode imputation
* Removed outliers using IQR method
* Converted date into:

  * Day of week
  * Month
  * Weekend indicator
* Encoded categorical variables using one-hot encoding
* Standardized numerical features using `StandardScaler`

---

## 🔍 Feature Engineering

Derived new features:

* Price ranges
* Age groups
* Review levels
* Weekend purchase indicator
* Late-night order indicator

---

## 🤖 Machine Learning Models

We implemented multiple models:

### 🔹 Logistic Regression

* Used as baseline model
* Provides probability-based predictions
* Easy to interpret

### 🔹 Decision Tree

* Captures complex patterns
* Higher accuracy but prone to overfitting

### 🔹 XGBoost (Final Model)

* Best performance
* Handles non-linear relationships
* Robust and scalable

---

## 📈 Model Evaluation

Metrics used:

* Accuracy
* Confusion Matrix
* Classification Report

We selected the final model based on:

* Accuracy
* Generalization ability
* Stability

---

## 🚀 Deployment (Streamlit)

We deployed the model using Streamlit to create an interactive web application.

### Features:

* User inputs:

  * Customer age
  * Product price
  * Quantity
  * Discount
  * Order time features
  * Category, payment method, location
* Real-time prediction
* Return probability output

---

## 🧩 System Architecture

User Input → Streamlit UI → Preprocessing (Scaler) → ML Model → Prediction → Output

---

## 🗄️ Database Integration

* Stored dataset using SQLite
* Normalized into:

  * Customers
  * Orders
  * Products
  * Transactions

---

## 📂 Project Structure

```
project/
│
├── app.py                 # Streamlit UI
├── train_model.py         # Model training script
├── model.pkl              # Trained model
├── scaler.pkl             # Scaler for preprocessing
├── final_ready_dataset.xlsx
├── README.md
```

---

## 🎤 Key Highlights

* End-to-end ML pipeline
* Feature engineering for better insights
* Real-time prediction system
* Clean UI for demonstration
* Scalable architecture

---

## 🔮 Future Improvements

* Deploy on cloud (AWS / Render)
* Add real-time data pipeline
* Improve model using ensemble methods
* Add explainability (SHAP values)

---

## 👨‍💻 Author

Malla Jeevan Kumar
CSE | NIT Nagaland

---

## ⭐ Conclusion

This project demonstrates how machine learning can be applied to solve real-world business problems by predicting product return behavior and improving decision-making.

---
