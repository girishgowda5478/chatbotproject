import json
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

nltk.download('punkt')

# Load intents
with open('intents.json') as file:
    data = json.load(file)

sentences = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        sentences.append(pattern)
        labels.append(intent['tag'])

# Convert text to vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

print("Model trained successfully!")
