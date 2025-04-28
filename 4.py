import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')

def get_semantic_relationships(word1, word2):
    synsets1 = wn.synsets(word1)
    synsets2 = wn.synsets(word2)
    if not synsets1 or not synsets2:
        return f"Semantic relationship could not be determined between {word1} and {word2}"
    synset1 = synsets1[0]
    synset2 = synsets2[0]

    relationships = {
        "Word 1": word1,
        "Word 2": word2,
        "Synset 1 Definition": synset1.definition(),
        "Synset 2 Definition": synset2.definition(),
        "Similarity Score": synset1.wup_similarity(synset2),
        "Hypernyms of Word 1": [lemma.name() for hypernym in synset1.hypernyms() for lemma in hypernym.lemmas()],
        "Hypernyms of Word 2": [lemma.name() for hypernym in synset2.hypernyms() for lemma in hypernym.lemmas()],
        "Hyponyms of Word 1": [lemma.name() for hyponym in synset1.hyponyms() for lemma in hyponym.lemmas()],
        "Hyponyms of Word 2": [lemma.name() for hyponym in synset2.hyponyms() for lemma in hyponym.lemmas()]
    }

    return relationships

word1 = "dog"
word2 = "cat"

semantic_relationships = get_semantic_relationships(word1, word2)

for key, value in semantic_relationships.items():
    print(f"{key}: {value}")
