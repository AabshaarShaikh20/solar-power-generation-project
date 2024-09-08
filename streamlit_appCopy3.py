#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import joblib

# Function to load model
def load_model():
    try:
        model = joblib.load('soloapowergeneration.pkl')
        st.write("Model loaded successfully!")
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please upload the model file.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

# Loading the saved model
model = load_model()

# Function to make predictions
def predict_power_generated(features):
    if model:
        df = pd.DataFrame([features])
        st.write("Features DataFrame:", df)  # Debug line
        try:
            prediction = model.predict(df)
            return prediction[0]
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
            return None
    else:
        st.error("Model is not loaded. Prediction cannot be performed.")
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
        st.error("Prediction failed. Please check the model and inputs.")

