import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and columns
with open("model/House_Price_Prediction.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/columns.pkl", "rb") as f:
    columns = pickle.load(f)

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏠 Bangalore House Price Prediction")
st.write("Predict house prices based on location and property details.")

# User inputs
location = st.selectbox("Location", sorted([c for c in columns if c not in ['total_sqft', 'bath', 'balcony', 'bhk']]))
total_sqft = st.number_input("Total Square Feet", min_value=300.0)
bhk = st.number_input("BHK", min_value=1)
bath = st.number_input("Bathrooms", min_value=1)
balcony = st.number_input("Balconies", min_value=0)

if st.button("Predict Price"):
    x = np.zeros(len(columns))
    x[columns.get_loc('total_sqft')] = total_sqft
    x[columns.get_loc('bath')] = bath
    x[columns.get_loc('balcony')] = balcony
    x[columns.get_loc('bhk')] = bhk

    if location in columns:
        x[columns.get_loc(location)] = 1

    price = model.predict([x])[0]

    st.success(f"💰 Estimated Price: ₹ {round(price, 2)} Lakhs")
