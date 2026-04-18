import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Return Risk Predictor", layout="wide")
st.title("Product Return Risk Predictor")

model  = joblib.load("models/logistic_regression_model.pkl")
scaler = joblib.load("models/scaler.pkl")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Product info")
    Product_Category    = st.selectbox("Product category", [0,1,2,3,4])
    Product_Price       = st.number_input("Product price (R$)", 10.0, 5000.0, 300.0, step=10.0)
    Order_Quantity      = st.number_input("Order quantity", 1, 20, 1)
    Discount_Applied    = st.number_input("Discount applied (R$)", 0.0, 500.0, 0.0, step=5.0)
    Price_Category      = st.selectbox("Price category", [0,1,2],
                            format_func=lambda x: ["Budget","Mid-range","Premium"][x])

    st.subheader("Order info")
    Payment_Method  = st.selectbox("Payment method", [0,1,2,3],
                        format_func=lambda x: ["Cash/COD","Credit card","Debit card","Net banking"][x])
    Shipping_Method = st.selectbox("Shipping method", [0,1,2],
                        format_func=lambda x: ["Standard","Express","Same day"][x])
    Order_Month     = st.selectbox("Order month", list(range(1,13)))
    Order_Weekday   = st.selectbox("Order weekday", list(range(7)),
                        format_func=lambda x: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][x])

with col2:
    st.subheader("Customer info")
    User_Age      = st.slider("User age", 18, 80, 30)
    User_Gender   = st.selectbox("User gender", [0,1],
                        format_func=lambda x: ["Male","Female"][x])
    User_Location = st.number_input("User location (zone ID)", 1, 100, 50)
    Age_Group     = st.selectbox("Age group", [0,1,2,3],
                        format_func=lambda x: ["Youth","Young adult","Adult","Senior"][x])

# Derived features
Is_Weekend         = 1 if Order_Weekday >= 5 else 0
Total_Value        = round((Product_Price * Order_Quantity) - Discount_Applied, 2)
Discount_Percentage= round((Discount_Applied / (Product_Price * Order_Quantity)) * 100, 4) \
                     if Product_Price > 0 else 0.0

st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Total value",      f"R$ {Total_Value:.2f}")
c2.metric("Discount %",       f"{Discount_Percentage:.2f}%")
c3.metric("Weekend order",    "Yes" if Is_Weekend else "No")

if st.button("Predict Return Risk", use_container_width=True):

    input_data = pd.DataFrame([{
        "Product_Category"   : Product_Category,
        "Product_Price"      : Product_Price,
        "Order_Quantity"     : Order_Quantity,
        "User_Age"           : User_Age,
        "User_Gender"        : User_Gender,
        "User_Location"      : User_Location,
        "Payment_Method"     : Payment_Method,
        "Shipping_Method"    : Shipping_Method,
        "Discount_Applied"   : Discount_Applied,
        "Total_Value"        : Total_Value,
        "Discount_Percentage": Discount_Percentage,
        "Price_Category"     : Price_Category,
        "Age_Group"          : Age_Group,
        "Order_Month"        : Order_Month,
        "Order_Weekday"      : Order_Weekday,
        "Is_Weekend"         : Is_Weekend,
    }])

    X_scaled  = scaler.transform(input_data)
    risk_prob = model.predict_proba(X_scaled)[0][1]
    risk_pct  = round(risk_prob * 100, 2)
    pred      = model.predict(X_scaled)[0]
    level     = "Low" if risk_pct < 25 else "Medium" if risk_pct < 55 else "High"

    st.divider()
    m1, m2, m3 = st.columns(3)
    m1.metric("Return risk %", f"{risk_pct}%")
    m2.metric("Risk level",    level)
    m3.metric("Prediction",    "Will Return" if pred==1 else "Safe")

    if level == "Low":
        st.success("Process order normally — low return risk detected.")
    elif level == "Medium":
        st.warning("Send a product confirmation email before shipping.")
    else:
        st.error("Flag for review — contact customer before dispatch!")

    with st.expander("See input vector sent to model"):
        st.dataframe(input_data)
        