from src.train import train_model
from src.predict import predict_news

# Train model
train_model()

# Test prediction
news = input("Enter news text: ")
result = predict_news(news)

print("Prediction:", result)