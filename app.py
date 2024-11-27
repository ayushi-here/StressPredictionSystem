import streamlit as st
from pages import Home, Predict, About, StressTips

# Set up the sidebar with the logo at the top and only one instance of navigation
st.sidebar.image("assets/logo.jpeg", use_column_width=True)
page = st.sidebar.radio("Navigate", ["Home", "Predict", "About", "Stress Tips"])

# Display the appropriate page based on navigation
if page == "Home":
    Home.display()

elif page == "Predict":
    Predict.display()

elif page == "About":
    About.display()

elif page == "Stress Tips":
    StressTips.display()
