import nltk
import numpy as np
import random
import json
import pickle
import tensorflow as tf
from nltk.stem import SnowballStemmer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from googlesearch import search


nltk.download("punkt")
stemmer = SnowballStemmer("french")

with open("intents.json", "r") as f:
    intents = json.load(f)

words = []
labels = []
docs_x = []
docs_y = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        docs_x.append(tokens)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
words = sorted(list(set(words)))
labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)

# Création du modèle de réseau neuronal
model = Sequential()
model.add(Dense(8, input_shape=(len(training[0]),), activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(len(output[0]), activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Entraînement du modèle
model.fit(training, output, epochs=1000, batch_size=8)

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
                
    return np.array(bag)

def chat():
    print("Démarrage du chatbot (taper 'quitter' pour arrêter)...")
    while True:
        inp = input("Vous: ")
        if inp.lower() == "quitter":
            break

        results = model.predict(np.array([bag_of_words(inp, words)]))
        results_index = np.argmax(results)
        tag = labels[results_index]

        for tg in intents["intents"]:
            if tg["tag"] == tag:
                responses = tg["responses"]
                response = random.choice(responses)

        if tag == "recherche":
            query = inp.replace("Recherche sur", "").replace("Cherche pour moi", "").replace("Peux-tu rechercher", "")
            print(response)
            for j in search(query, num_results=3):
                print(j)
        else:
            print(response)

chat()


chat()
