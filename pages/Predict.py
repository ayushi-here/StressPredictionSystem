import streamlit as st
from helper import load_vectorizer, load_model, text_process

# Load model and vectorizer
vectorizer = load_vectorizer(vectorizer_type='tfidf')  # Use TF-IDF for vectorization
model = load_model()

def predictor(text):
    """Predict stress from input text and return the prediction label and confidence."""
    processed_text = text_process(text)
    embedded_text = vectorizer.transform([processed_text])
    prediction = model.predict(embedded_text)
    confidence = model.predict_proba(embedded_text)[0][prediction[0]] * 100  # Confidence in percentage
    return prediction[0], confidence

def display():
    """Display the Predict page with updated UI and prediction output."""
    st.title("Stress Prediction")
    # st.image("assets/logo.jpeg", use_column_width=True, caption="Stress Prediction")

    # Background Image
    st.markdown(
        f'<div style="background-image: url(assets/background.png); background-size: cover; padding: 20px; color: white;">',
        unsafe_allow_html=True
    )

    input_text = st.text_area("Enter text to predict stress:")
    
    if st.button("Predict"):
        if input_text.strip():
            prediction, confidence = predictor(input_text)
            result = "This person is in stress." if prediction == 1 else "This person is not in stress."
            
            # Display prediction and confidence
            st.subheader(f"Prediction: {result}")
            st.write(f"Confidence Level: {confidence:.2f}%")

        else:
            st.error("Please enter some text to analyze.")
    
    st.markdown("</div>", unsafe_allow_html=True)
