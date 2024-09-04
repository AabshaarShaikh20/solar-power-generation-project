#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load('soloar.pkl')

# Function to make predictions
def predict_power_generated(features):
    prediction = model.predict([features])
    return prediction[0]

# Streamlit app interface
st.title('Energy Production Prediction')

st.header('Enter Environmental Variables')

# Input fields for user data
distance_to_solar_noon = st.slider('Distance to Solar Noon', min_value=0.0, max_value=100.0, value=50.0)
temperature = st.slider('Temperature', min_value=-30.0, max_value=50.0, value=20.0)
wind_direction = st.slider('Wind Direction', min_value=0, max_value=360, value=180)
wind_speed = st.slider('Wind Speed', min_value=0.0, max_value=150.0, value=10.0)
sky_cover = st.slider('Sky Cover', min_value=0.0, max_value=1.0, value=0.5)
visibility = st.slider('Visibility', min_value=0.0, max_value=10.0, value=5.0)
humidity = st.slider('Humidity', min_value=0.0, max_value=100.0, value=50.0)
average_wind_speed = st.slider('Average Wind Speed', min_value=0.0, max_value=150.0, value=10.0)
average_pressure = st.slider('Average Pressure', min_value=950.0, max_value=1050.0, value=1013.25)

# Arrange the inputs into a single list
features = [distance_to_solar_noon, temperature, wind_direction, wind_speed,
            sky_cover, visibility, humidity, average_wind_speed, average_pressure]

# Prediction button
if st.button('Predict'):
    prediction = predict_power_generated(features)
    st.success(f'Estimated Power Generated: {prediction:.2f} Joules')


# In[ ]:




