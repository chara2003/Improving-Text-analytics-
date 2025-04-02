import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\d+", "", text)  # Remove numbers (optional)
    text = re.sub(r"[^\w\s-]", "", text)  # Remove punctuation except hyphens
    tokens = word_tokenize(text)  # Tokenize
    stop_words = set(stopwords.words("english"))
    cleaned_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(cleaned_tokens)

# Get user input
user_text = input("Enter your text: ")
cleaned_text = clean_text(user_text)

# Display output
from tabulate import tabulate
table = [[user_text, cleaned_text]]
print(tabulate(table, headers=["Original Text", "Cleaned Text"], tablefmt="grid"))
