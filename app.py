import streamlit as st
import joblib
import numpy as np
import re
from sklearn.preprocessing import StandardScaler
import warnings
from scipy.sparse import hstack

# Ignore user warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load the TF-IDF vectorizer
tfidf = joblib.load('tfidf_vectorizer.pkl')  # Save this during training

# Mapping sentiment labels
sentiment_map = {-1: 'Anti', 0: 'Neutral', 1: 'Pro', 2: 'News'}

# Text cleaning function
def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)
    text = text.lower()
    return text

def preprocess_input(text):
    cleaned = clean_text(text)
    length = len(cleaned.split())
    X_tfidf = tfidf.transform([cleaned])
    X_input = hstack([X_tfidf, np.array([[length]])])
    X_scaled = scaler.transform(X_input)
    return X_scaled

# Streamlit UI
st.title("🌍 Climate Change Sentiment Analysis")
st.write("Enter a tweet and see its sentiment:")

tweet = st.text_area("Tweet Text")

if st.button("Analyze"):
    if tweet.strip() == "":
        st.error("Please enter a tweet!")
    else:
        # Clean and process text
        X = preprocess_input(tweet)
        
        # Predict sentiment
        pred = model.predict(X)[0]
        sentiment = sentiment_map.get(pred, "Unknown")
        
        st.write("### ✅ Sentiment Result:")
        st.write(f"**{sentiment}**")
