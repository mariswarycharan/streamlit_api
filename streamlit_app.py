import streamlit as st
import requests

# Make an API call
response = requests.get('http://localhost:5000/api/data')
api_data = response.json()

# Display the API response in Streamlit
st.write("API Response:", api_data['message'])
