import spacy

nlp = spacy.load("en_core_web_sm")
text = "Apple CEO Tim Cook announced new iPhone models in California yesterday"
doc = nlp(text)

predictions = [(ent.text, ent.label_) for ent in doc.ents]

for text, label in predictions:
    print(f"{text}: {label}")
