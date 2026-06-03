import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load("random_forest_model.pkl")  # best performing model

st.title("💧 Water Potability Predictor")
st.write("Enter the water quality parameters below to check if the water is safe to drink.")

# Input fields
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", value=150.0)
solids = st.number_input("Solids", value=20000.0)
chloramines = st.number_input("Chloramines", value=7.0)
sulfate = st.number_input("Sulfate", value=333.0)
conductivity = st.number_input("Conductivity", value=400.0)
organic_carbon = st.number_input("Organic Carbon", value=14.0)
trihalomethanes = st.number_input("Trihalomethanes", value=66.0)
turbidity = st.number_input("Turbidity", value=3.9)

if st.button("Predict"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ This water is POTABLE (Safe to drink)")
    else:
        st.error("❌ This water is NOT POTABLE (Unsafe to drink)")
