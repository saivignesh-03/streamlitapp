import json
import streamlit as st
import requests

# Define the feature names and initialize the user inputs
feature_names = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
    "compactness_mean", "concavity_mean", "concave_points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se", 
    "compactness_se", "concavity_se", "concave_points_se", "symmetry_se", "fractal_dimension_se",
    "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst",
    "compactness_worst", "concavity_worst", "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"
]

# Title of the Streamlit app
st.title('Breast Cancer Prediction')

# Create a dictionary to collect user inputs
user_inputs = {}

# Sidebar sliders for user input for each feature
st.sidebar.header("Input Features")
for feature in feature_names:
    user_inputs[feature] = st.sidebar.number_input(feature, value=0.0)

# Show the user inputs for review
st.write("### Input Data:")
st.json(user_inputs)

# Button to make the prediction
if st.button('Predict'):
    # Prepare data for the API
    data = {
        "inputs": user_inputs
    }

    try:
        # Send POST request to the FastAPI endpoint
        response = requests.post('http://206.189.206.28:8000/predict/', json=data)  # Replace with your API's endpoint
        
        if response.status_code == 200:
            # Display the prediction result
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
