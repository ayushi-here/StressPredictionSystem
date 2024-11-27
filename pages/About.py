import streamlit as st

def display():
    """Display the About page with a clean layout."""
    st.title("About Stress Prediction App")
    # st.image("assets/logo.jpeg", use_column_width=True, caption="Our Logo")

    # Background Image
    st.markdown(
        f'<div style="background-image: url(assets/background.png); background-size: cover; padding: 20px; color: white;">',
        unsafe_allow_html=True
    )
    
    st.markdown("""
    ### About This App
    The Stress Prediction App leverages machine learning and natural language processing to predict stress levels based on text input.  
    This predictive model helps people identify signs of stress in their communication and offers actionable insights to manage mental health better.

    **How Does It Work?**
    The app uses advanced NLP techniques to analyze the input text and identify keywords and patterns that indicate stress. The model then provides a prediction based on this analysis. This can help users take early action to manage stress.

    **Key Features:**
    - **NLP-based Prediction**: The app uses state-of-the-art text analysis to predict stress levels.
    - **Simple Interface**: The app has an easy-to-use interface for text input and displays results in a straightforward manner.
    - **Real-Time Feedback**: Users can immediately know if they’re experiencing stress based on their input text.
    - **Help and Tips**: Once the user identifies the stress level, the app provides useful tips to manage stress.

    ### Why is this important?
    Stress is one of the leading causes of mental and physical health issues worldwide. By identifying stress early, we can manage it better and improve our well-being.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
