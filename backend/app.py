import streamlit as st
import pandas as pd
import requests

# Set page config for a professional look
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

st.title("❤️ Heart Disease Prediction Dashboard")
st.write("Enter the patient's medical details below to predict the risk of heart disease.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 1, 100, 45)
    sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", value=120)
    chol = st.number_input("Serum Cholestoral (mg/dl)", value=200)

with col2:
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "True" if x == 1 else "False")
    restecg = st.selectbox("Resting ECG Results", options=[0, 1, 2])
    thalach = st.number_input("Maximum Heart Rate Achieved", value=150)
    exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Predict Button
if st.button("Predict Health Status"):
    # This prepares the data to send to your FastAPI backend
    input_data = {
        "age": age,
        "sex": sex,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang
    }
    
    # Placeholder for prediction logic
    # Once your FastAPI is live, you replace this with: 
    # response = requests.post("YOUR_API_URL/predict", json=input_data)
    
    st.success("Model Analysis Complete!")
    st.balloons()
    st.write("### Result: Low Risk") 
    st.info("Note: This is a demo. Ensure your model .pkl is linked for live inference.")
