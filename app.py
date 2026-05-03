import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="House Price Predictor", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: green;'>🏠 House Price Prediction Dashboard</h1>", unsafe_allow_html=True)

st.write("### Enter Property Details Below:")

# Layout in columns
col1, col2 = st.columns(2)

with col1:
    square_ft = st.slider("Square Feet", 100, 5000, 1000)
    bhk = st.slider("BHK", 1, 10, 2)

    under_construction = st.selectbox("Under Construction", [0, 1])
    rera = st.selectbox("RERA Approved", [0, 1])
    ready_to_move = st.selectbox("Ready to Move", [0, 1])
    resale = st.selectbox("Resale", [0, 1])

with col2:
    longitude = st.number_input("Longitude", value=77.0)
    latitude = st.number_input("Latitude", value=28.0)

    posted_by = st.radio("Posted By", ["Dealer", "Owner"])
    bhk_type = st.radio("BHK Type", ["BHK", "RK"])

# Encoding
posted_by_dealer = 1 if posted_by == "Dealer" else 0
posted_by_owner = 1 if posted_by == "Owner" else 0
bhk_or_rk = 1 if bhk_type == "RK" else 0

st.markdown("---")

# Prediction
if st.button("🚀 Predict Price"):
    
    features = np.array([[under_construction, rera, bhk, square_ft,
                          ready_to_move, resale, longitude, latitude,
                          posted_by_dealer, posted_by_owner, bhk_or_rk]])
    
    prediction = model.predict(features)
    price = prediction[0]

    st.success(f"💰 Predicted Price: {price:.2f} Lakhs")

    # Simple visualization
    st.write("### 📊 Price Visualization")
    st.bar_chart([price])