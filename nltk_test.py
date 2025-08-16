import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
print(word_tokenize("This is a test."))