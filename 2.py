import spacy
from sklearn.metrics import classification_report

def predict_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
    
def evaluate_ner(texts_and_labels):
    true_labels = []
    pred_labels = []

    for text, true_ents in texts_and_labels:
        preds = predict_entities(text)
        true_labels.extend([label for _, label in true_ents])
        pred_labels.extend([label for _, label in preds])

    return classification_report(true_labels, pred_labels)

text = "Apple CEO Tim Cook announced new iPhone models in California yesterday"
print("\nExample Text Entities:\n")
for text, label in predictions:
    print(f"{text}: {label}")

test_data = [
    (
        "Microsoft's Satya Nadella visited London.",
        [("Micorosft", "ORG"), ("Satya Nadella", "PERSON"), ("London", "GPE")]
    ),
    (
        "Google opened a new office in Paris.",
        [("Micorosft", "ORG"), ("Paris", "GPE")]
    )
]

print("\nEvaluation")
print(evaluate_ner(test_data))
