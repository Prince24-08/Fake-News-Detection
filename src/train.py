from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

from src.data_loader import load_data
from src.preprocessing import clean_text
from src.vectorizer import get_vectorizer
from src.model import get_model

def train_model():
    data = load_data()
    data["text"] = data["text"].apply(clean_text)

    X = data["text"]
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    vectorizer = get_vectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = get_model()
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)
    print("Accuracy:", accuracy_score(y_test, y_pred))

    # Save model
    pickle.dump(model, open("models/model.pkl", "wb"))
    pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))