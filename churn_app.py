import streamlit as st
import requests
from streamlit_lottie import st_lottie

#Set cofiguration
st.set_page_config(
    page_title = "Machine Learning Classification Prediction",
    page_icon = ":shark:",
    layout = "wide"

)

# Set the title of the app
st.title('Telco Customer Churn Prediction App')

# Add a header for the homepage
st.header('Welcome to the Telco Customer Churn Prediction Dev App')

# Add a brief overview or introduction
st.write("""
## Overview
This page provides insights and predictions regarding customer churn for a telecommunications company.
Explore the sections below to gain a deeper understanding of the data and the model.
""")

# Load a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Example Lottie animation related to customer churn/retention
lottie_animation = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_touohxv0.json")  # Example URL

# Display the Lottie animation

# Key Features Section
st.write("## Key Features")
st.write("""
- **Data Analysis**: Explore and analyze customer data to uncover patterns related to churn.
- **Predictive Modeling**: Leverage machine learning models to predict the likelihood of customer churn.
- **Interactive Dashboards**: Visualize key metrics and KPIs through interactive dashboards.
- **User-Friendly Interface**: Simple and intuitive design for easy navigation and understanding.
""")

# App Features Section
st.write("## App Features")
st.write("""
    - Customer demographics and behavior analysis
    - Customer segmentation
    - Predictive churn risk assessment
    - Comprehensive reporting and dashboards
""")

# Social Links
st.write("### Connect with Me")
st.write("[GitHub](https://github.com/yourusername)")
st.write("[LinkedIn](https://www.linkedin.com/in/yourprofile/)")
st.write("[Medium](https://medium.com/@yourprofile)")

# Source Code Link
st.write("### Source Code")
st.write("[Check out the source code on GitHub](https://github.com/yourusername/telco-churn-app)")

# Add a sidebar with navigation options or settings
st.sidebar.success("Use the sidebar to navigate")



