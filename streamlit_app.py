import json
import streamlit as st
import requests

# Define the feature names and their initial values
features = {
    "radius_mean": 28.0,
    "texture_mean": 35.0,
    "perimeter_mean": 180.0,
    "area_mean": 1500.0,
    "smoothness_mean": 0.200,
    "compactness_mean": 0.400,
    "concavity_mean": 0.550,
    "concave_points_mean": 0.300,
    "symmetry_mean": 0.450,
    "fractal_dimension_mean": 0.150,
    "radius_se": 0.350,
    "texture_se": 0.450,
    "perimeter_se": 0.600,
    "area_se": 0.800,
    "smoothness_se": 0.100,
    "compactness_se": 0.250,
    "concavity_se": 0.350,
    "concave_points_se": 0.500,
    "symmetry_se": 0.700,
    "fractal_dimension_se": 0.120,
    "radius_worst": 25.0,
    "texture_worst": 40.0,
    "perimeter_worst": 200.0,
    "area_worst": 1800.0,
    "smoothness_worst": 0.250,
    "compactness_worst": 0.450,
    "concavity_worst": 0.600,
    "concave_points_worst": 0.400,
    "symmetry_worst": 0.550,
    "fractal_dimension_worst": 0.200
}

# Title of the Streamlit app
st.title('Breast Cancer Prediction')

# Create a dictionary to collect user inputs
user_inputs = {}

# Sidebar sliders for user input for each feature
st.sidebar.header("Input Features")
for feature, default_value in features.items():
    user_inputs[feature] = st.sidebar.number_input(feature, value=default_value)

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
