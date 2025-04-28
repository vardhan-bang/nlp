import nltk
from nltk.util import ngrams
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('punkt')

text = """
Natural Language Processing (NLP) enables computers to understand human language. 
By analyzing text patterns, machines can interpret and respond to user input more effectively.
"""

tokens = nltk.word_tokenize(text.lower())

def analyze_ngrams(tokens, n, title):
    n_grams = list(ngrams(tokens, n))
    n_gram_counts = Counter(n_grams)
    
    print(f"Top {n}-grams:")
    for gram, count in n_gram_counts.most_common(10):
        print(f"{' '.join(gram)}: {count}")
    
    grams = [' '.join(gram) for gram, count in n_gram_counts.most_common(10)]
    counts = [count for gram, count in n_gram_counts.most_common(10)]
    
    plt.figure(figsize=(10,5))
    plt.barh(grams, counts, color='skyblue')
    plt.title(f"Top {n}-grams - {title}")
    plt.gca().invert_yaxis()
    plt.show()

analyze_ngrams(tokens, 1, "Unigram Analysis")
analyze_ngrams(tokens, 2, "Bigram Analysis")
analyze_ngrams(tokens, 3, "Trigram Analysis")
