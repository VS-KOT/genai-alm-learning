import sys
import os
import streamlit as st
from services.temprature_api import get_weather



st.title("🌤 Weather App")

latitude = st.text_input("Enter Latitude")
longitude = st.text_input("Enter Longitude")

if st.button("Get Weather"):
    if latitude and longitude:
        weather = get_weather(latitude, longitude)
        st.success(f"Temperature: {weather['temperature']} °C")
        st.info(f"Wind Speed: {weather['wind_speed']} km/h")
    else:
        st.error("Please enter latitude and longitude")