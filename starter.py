import streamlit as st
import joblib
import pandas as pd

# load model
pipe = joblib.load('model/model.joblib')

st.title("Car Price Predictor - Canada")

# Input fields
make = st.selectbox("Make", ["Honda", "Toyota", "Suzuki", "Mercedes-Benz"])
model_name = st.text_input("Model")
year = st.number_input("Year", 1990, 2024, 2010)
miles = st.number_input("Miles", 0, 1000000, 50000)
body_type = st.selectbox("Body Type", ["Sedan", "SUV", "Hatchback", "Truck"])
vehicle_type = st.selectbox("Vehicle Type", ["New", "Used"])
drivetrain = st.selectbox("Drivetrain", ["AWD", "FWD", "RWD"])
transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
fuel_type = st.selectbox("Fuel Type", ["Gasoline", "Hybrid", "Electric"])
engine_block = st.selectbox("Engine Block", ["Aluminum", "Cast Iron"])
engine_size = st.number_input("Engine Size", 1.0, 8.0, 2.0, 0.1)
state = st.selectbox("State", ["ON", "QC", "BC", "AB", "NB"])

if st.button("Calculate"):
    input_data = {
        "year": [year],
        "miles": [miles],
        "make": [make.lower()],
        "model": [model_name.lower()],
        "body_type": [body_type.lower()],
        "vehicle_type": [vehicle_type.lower()],
        "drivetrain": [drivetrain.lower()],
        "transmission": [transmission.lower()],
        "fuel_type": [fuel_type.lower()],
        "engine_block": [engine_block.lower()],
        "engine_size": [engine_size],
        "state": [state.lower()]
    }

    try:
        X_pred = pd.DataFrame(input_data)
        pred = pipe.predict(X_pred)[0]
        st.success(f"**Predicted Price: ${pred:,.2f} CAD**")
    except ValueError:
        st.error("Sorry, ye Make/Model abhi available nahi. Honda/Toyota try karo.")