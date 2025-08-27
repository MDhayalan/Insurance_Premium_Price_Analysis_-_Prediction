import streamlit as st
import numpy as np
import joblib

# ---- Load trained model ----
model = joblib.load("premium_model.pkl")  # Make sure model.pkl is in same folder

# ---- Custom CSS ----
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Aptos&display=swap');
    
    body {
        background: linear-gradient(45deg, #e7fbe9, #caf4d7, #b9f2ca);
        font-family: 'Aptos', sans-serif;
        color: white;
    }
    .stApp {
        background: linear-gradient(45deg, #e7fbe9, #caf4d7, #b9f2ca);
    }
    h1 {
        text-align: center;
        font-weight: 800;
        font-size: 28px;
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .result-box {
        background: rgba(185, 255, 202, 0.08);
        border-radius: 12px;
        padding: 15px;
        margin: 20px 0;
        font-size: 20px;
        font-weight: bold;
        color: #05874b;
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 15px;
        color: #150ee8;
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown("<h1>Insurance Premium Prediction</h1>", unsafe_allow_html=True)

# ---- Input Section ----
col1, col2 = st.columns(2)

# User inputs

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=1)
    height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1)
    diabetes = st.radio("Diabetes", ["Yes", "No"], horizontal=True)
    bp = st.radio("Blood Pressure Problems", ["Yes", "No"], horizontal=True)
    transplant = st.radio("Any Transplants?", ["Yes", "No"], horizontal=True)
    

with col2:
    weight = st.number_input("Weight (Kg)", min_value=1.0, max_value=150.0, value=1)
    bmi = weight / (height**2)
    NumberOfMajorSurgeries = st.number_input("Number Of Major Surgeries", min_value=0, max_value=10, value=0)
    chronic = st.radio("Any Chronic Diseases? ", ["Yes", "No"], horizontal=True)
    allergy = st.radio("Any Allergies", ["Yes", "No"], horizontal=True)
    cancer = st.radio("History of Cancer in Family?", ["Yes", "No"], horizontal=True)

def encode(val): 
    return 1 if val == "Yes" else 0

X_input = np.array([[
    age,
    encode(diabetes),
    encode(bp),
    encode(transplant),
    encode(chronic),
    height,
    weight,
    encode(allergy),
    encode(cancer),
    NumberOfMajorSurgeries,
    bmi 
   
    
]])

# ---- Prediction Button ----
if st.button("Predict Premium"):
    try:
        prediction = model.predict(X_input)[0]
        st.markdown(
            f"<div class='result-box'>✅ Predicted Insurance Premium: ₹ {prediction:,.2f}</div>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Error in prediction: {e}")

# ---- Footer ----
st.markdown("""
    <div class="footer">
        Developed by Dhayalan © 2025 <br>
        📧 Contact: <a href="mailto:dhaya25@outlook.com" style="color:#150ee8;">dhaya25@outlook.com</a>  | 
        🔗 Profile: <a href="https://mdhayalan.github.io/" style="color:#150ee8;">Click Here</a>
    </div>
""", unsafe_allow_html=True)

