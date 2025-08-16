import nltk
nltk.download('punkt', force=True)
nltk.download('wordnet', force=True)
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    # Placeholder: return all tokens as symptoms
    return lemmas