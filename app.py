import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Predictor")

st.write(
    "Predict house prices using machine learning."
)

st.sidebar.header("Property Features")

OverallQual = st.sidebar.slider(
    "Overall Quality",
    min_value=1,
    max_value=10,
    value=5
)

TotalHouseSF = st.sidebar.number_input(
    "Total House Area (sq ft)",
    min_value=0,
    value=2000
)

GarageCars = st.sidebar.number_input(
    "Garage Capacity",
    min_value=0,
    value=2
)

TotalBath = st.sidebar.number_input(
    "Total Bathrooms",
    min_value=0.0,
    value=2.0,
    step=0.5
)

ExterQual = st.sidebar.slider(
    "Exterior Quality",
    min_value=1,
    max_value=5,
    value=3
)

KitchenQual = st.sidebar.slider(
    "Kitchen Quality",
    min_value=1,
    max_value=5,
    value=3
)

BsmtQual = st.sidebar.slider(
    "Basement Quality",
    min_value=1,
    max_value=5,
    value=3
)

YearBuilt = st.sidebar.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2000
)


st.subheader("Selected Features")

col1, col2 = st.columns(2)

with col1:
    st.write("Overall Quality:", OverallQual)
    st.write("Total House Area:", TotalHouseSF)
    st.write("Garage Capacity:", GarageCars)
    st.write("Total Bathrooms:", TotalBath)

with col2:
    st.write("Exterior Quality:", ExterQual)
    st.write("Kitchen Quality:", KitchenQual)
    st.write("Basement Quality:", BsmtQual)
    st.write("Year Built:", YearBuilt)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "OverallQual": [OverallQual],
        "TotalHouseSF": [TotalHouseSF],
        "GarageCars": [GarageCars],
        "TotalBath": [TotalBath],
        "ExterQual": [ExterQual],
        "KitchenQual": [KitchenQual],
        "BsmtQual": [BsmtQual],
        "YearBuilt": [YearBuilt]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated House Price: ${prediction[0]:,.0f}"
    )


