import streamlit as st

def display():
    """Display Stress Tips page with clean tips and contact info."""
    st.title("Tips to Deal with Stress")
    # st.image("assets/logo.jpeg", use_column_width=True, caption="Our Logo")

    # Background Image
    st.markdown(
        f'<div style="background-image: url(assets/background.png); background-size: cover; padding: 20px; color: white;">',
        unsafe_allow_html=True
    )

    st.subheader("1. Practice Deep Breathing")
    st.write("""
        Deep breathing exercises are a quick and effective way to calm the nervous system and reduce stress.  
        A simple exercise is to breathe in for 4 seconds, hold your breath for 4 seconds, and exhale for 4 seconds. Repeat several times until you feel more relaxed.
    """)

    st.subheader("2. Regular Physical Activity")
    st.write("""
        Physical activity releases endorphins, which are chemicals in your brain that act as natural mood elevators.  
        Aim for at least 30 minutes of exercise most days of the week. Whether it's a walk, jog, or yoga, staying active helps you cope with stress more effectively.
    """)

    st.subheader("3. Stay Connected with Loved Ones")
    st.write("""
        Social support plays a crucial role in managing stress. Share your feelings with family, friends, or colleagues.  
        Isolation can worsen stress, so staying connected with your support network is important for your mental well-being.
    """)

    st.subheader("4. Engage in Mindfulness or Meditation")
    st.write("""
        Mindfulness and meditation can help you stay present and calm. Techniques such as focusing on your breath or practicing guided meditation can reduce anxiety and improve emotional regulation.
    """)

    st.subheader("5. Seek Professional Help if Necessary")
    st.write("""
        If stress becomes overwhelming, it’s important to seek help from a professional. They can guide you through stress management strategies and provide resources to improve your mental health.
    """)

    # Contact Info
    st.write("""
    ### Professional Help Contacts:
    - **Dr. John Doe** - Psychologist  
      Phone: 123-456-7890  
    - **Dr. Jane Smith** - Psychiatrist  
      Phone: 987-654-3210
    """)

    st.markdown("</div>", unsafe_allow_html=True)
