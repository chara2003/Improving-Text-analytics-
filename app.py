import streamlit as st
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download("stopwords")
nltk.download("punkt")

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = re.sub(r"[^\w\s-]", "", text)  # Remove punctuation except hyphens
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    cleaned_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(cleaned_tokens)

# Streamlit UI
st.title("📝 Text Preprocessing Tool")

user_text = st.text_area("Enter your text here:")
if st.button("Process Text"):
    if user_text.strip():
        cleaned_text = clean_text(user_text)
        st.success("✅ Text Processed Successfully!")
        st.write("### Cleaned Text:")
        st.write(cleaned_text)
    else:
        st.warning("⚠️ Please enter some text!")
