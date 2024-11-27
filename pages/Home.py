import streamlit as st

def display():
    """Display the Home page with a clean layout and landscape welcome image."""
    st.title("Welcome to the Stress Prediction App")
    st.image("assets/welcome.jpeg", use_column_width=True, caption="Identify Stress with AI", output_format="JPEG")
    
    # Background Image
    st.markdown(
        f'<div style="background-image: url(assets/background.png); background-size: cover; padding: 20px; color: white;">',
        unsafe_allow_html=True
    )
    st.markdown("""
    **Stress is a mental state that can affect our thoughts, feelings, and behavior.**  
    In this modern world, stress is an inevitable part of life. Stress can affect everyone, but how you respond to it can determine its impact on your mental and physical health. 
    Our app helps you identify if you are experiencing stress based on your written text.

    ### How This App Works
    The app uses machine learning and natural language processing (NLP) to analyze the text you provide and predicts if you are experiencing stress. By identifying signs of stress in your communication, you can take steps to address it early.

    **Features of this App:**
    - Stress Detection using advanced machine learning techniques.
    - Simple and intuitive interface to make predictions easily.
    - Useful tips on dealing with stress and maintaining mental health.

    Explore the app further by navigating to the **Predict**, **About**, or **Stress Tips** pages in the sidebar.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
