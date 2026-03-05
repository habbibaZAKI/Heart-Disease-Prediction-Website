import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️")

st.title("❤️ Heart Disease Prediction")
st.write("Logged in as: " + st.session_state.get('user_email', 'Guest User'))

# Match your HTML structure with two columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", value=25)
    sex = st.selectbox("Sex (0=Female, 1=Male)", [0, 1])
    cp = st.slider("Chest Pain Type (0-3)", 0, 3, 0)
    trestbps = st.number_input("Resting Blood Pressure", value=120)
    chol = st.number_input("Cholesterol", value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", [0, 1])

with col2:
    restecg = st.slider("Resting ECG (0-2)", 0, 2, 0)
    thalach = st.number_input("Max Heart Rate Achieved", value=150)
    exang = st.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [0, 1])
    oldpeak = st.number_input("Oldpeak (ST depression)", value=0.0, step=0.1)
    slope = st.slider("Slope (0-2)", 0, 2, 0)
    ca = st.slider("Major Vessels (0-3)", 0, 3, 0)
    thal = st.slider("Thal (1-3)", 1, 3, 1)

if st.button("Predict"):
    # This structure matches your 'const data' in HTML
    feature_data = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
        "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
        "exang": exang, "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }

    # This matches your FastAPI 'PredictionRequest' model
    payload = {
        "user_email": "zakihabiba59@gmail.com",
        "data": feature_data
    }

    st.info("Sending data to your FastAPI backend...")
    
    # When your backend is deployed, replace the URL below
    # try:
    #     response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    #     result = response.json()
    #     st.success(f"Prediction Result: {result['prediction']}")
    # except Exception as e:
    #     st.error("Could not connect to FastAPI backend. Make sure it is running!")
