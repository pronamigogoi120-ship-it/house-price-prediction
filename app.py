import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction")

st.write("Enter details:")

# Inputs
square_ft = st.number_input("Square Feet", min_value=100)
bhk = st.number_input("BHK", min_value=1)

under_construction = st.selectbox("Under Construction", [0,1])
rera = st.selectbox("RERA Approved", [0,1])
ready_to_move = st.selectbox("Ready to Move", [0,1])
resale = st.selectbox("Resale", [0,1])

longitude = st.number_input("Longitude", value=77.0)
latitude = st.number_input("Latitude", value=28.0)

posted_by = st.selectbox("Posted By", ["Dealer", "Owner"])
bhk_type = st.selectbox("BHK Type", ["BHK", "RK"])

# Convert inputs
posted_by_dealer = 1 if posted_by == "Dealer" else 0
posted_by_owner = 1 if posted_by == "Owner" else 0
bhk_or_rk = 1 if bhk_type == "RK" else 0

# Prediction
if st.button("Predict Price"):
    
    features = np.array([[under_construction, rera, bhk, square_ft,
                          ready_to_move, resale, longitude, latitude,
                          posted_by_dealer, posted_by_owner, bhk_or_rk]])
    
    prediction = model.predict(features)
    
    st.success(f"💰 Predicted Price: {prediction[0]:.2f} Lakhs")