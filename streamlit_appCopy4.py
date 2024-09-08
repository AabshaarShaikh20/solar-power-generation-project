#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import joblib

# Loading the saved model
try:
    model = joblib.load('soloapowergeneration.pkl')
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

# Function to make predictions
def predict_power_generated(features):
    df = pd.DataFrame([features])
    try:
        prediction = model.predict(df)
        return prediction[0]
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        return None

# Streamlit app
st.title("Solar Power Generation Prediction")

st.write("Enter the environmental variables to predict the solar power generation:")

# User input
distance_to_solar_noon = st.number_input("Distance to Solar Noon (minutes)")
temperature = st.number_input("Temperature (°C)")
wind_direction = st.number_input("Wind Direction (°)")
wind_speed = st.number_input("Wind Speed (km/h)")
sky_cover = st.number_input("Sky Cover (oktas)")
visibility = st.number_input("Visibility (km)")
humidity = st.number_input("Humidity (%)")
average_wind_speed = st.number_input("Average Wind Speed (km/h)")
average_pressure = st.number_input("Average Pressure (hPa)")

# Prediction button
if st.button("Predict"):
    features = {
        "distance-to-solar-noon": distance_to_solar_noon,
        "temperature": temperature,
        "wind-direction": wind_direction,
        "wind-speed": wind_speed,
        "sky-cover": sky_cover,
        "visibility": visibility,
        "humidity": humidity,
        "average-wind-speed-(period)": average_wind_speed,
        "average-pressure-(period)": average_pressure
    }
    
    prediction = predict_power_generated(features)
    
    if prediction is not None:
        st.success(f"Predicted Power Generated: {prediction:.2f} kW")
    else:
        st.error("Prediction could not be made. Please check the model and inputs.")

