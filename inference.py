import pickle
import numpy as np
def classify(text):
    model = pickle.load(open('model.pkl','rb'))
    vectorizer = pickle.load(open('vectorizer.pkl','rb'))
    text = vectorizer.transform([text])
    return model.predict(text)[0]


