import pickle
import re
from urllib.parse import urlparse
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize components
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def load_vectorizer(vectorizer_type='tfidf'):
    """Load the vectorizer."""
    try:
        filename = f"{vectorizer_type}_vectorizer.pkl"
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not found.")

def load_model():
    """Load the saved model."""
    try:
        with open('model.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Model file not found.")

def text_process(text):
    """Preprocess the input text."""
    text = re.sub(r'[][)(]', ' ', text)
    text = ' '.join(word for word in text.split() if not urlparse(word).scheme)
    text = re.sub(r'\@\w+', '', text)
    text = re.sub(re.compile('<.*?>'), '', text)
    text = re.sub(r'[^A-Za-z0-9]', ' ', text)
    text = text.lower()
    text = ' '.join(word.strip() for word in text.split())
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(lemmatizer.lemmatize(word) for word in tokens)
