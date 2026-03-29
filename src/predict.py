import pickle
from src.preprocessing import clean_text

def load_model():
    model = pickle.load(open("models/model.pkl", "rb"))
    vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
    return model, vectorizer

def predict_news(text):
    model, vectorizer = load_model()
    text = clean_text(text)
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)

    return "Real News" if prediction[0] == 1 else "Fake News"