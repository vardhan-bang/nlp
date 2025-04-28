python -m spacy download en

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import spacy

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

nlp = spacy.load("en_core_web_sm")

text = "The cats are happily running towards the biggest playground"

tokens = word_tokenize(text)
print("Tokens: ", tokens)

stemmer = PorterStemmer()
stems = [stemmer.stem(token) for token in tokens]
print("Stemming: ", stems)

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token.lower(), pos = 'v') for token in tokens]
print("Lemmatization: ", lemmas)

doc = nlp(text)
print("\nMorphological analysis using spacy")
for token in doc:
    print(f"{token.text}: {token.lemma_} ({token.pos_}) -> {token.morph}")
