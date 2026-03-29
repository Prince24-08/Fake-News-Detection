Fake News Detection System

Overview

I built this project to spot fake news using machine learning and natural language processing (NLP). The system learns from a dataset packed with real and fake news articles, then uses TF-IDF and logistic regression to figure out which is which.

Problem Statement

Let’s be real—fake news spreads fast online and throws people off. This project sets out to automatically sort news articles as real or fake, just by analyzing their content.

Features

- Cleans up and preps the text
- Pulls out key features with TF-IDF
- Classifies news using a machine learning model
- Makes predictions in real time from whatever the user enters
- Keeps the code neat and modular

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLP (TF-IDF)

Project Structure

fake-news-detection/
│
├── data/
│   ├── Fake.csv
│   └── True.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── vectorizer.py
│   ├── model.py
│   ├── train.py
│   └── predict.py
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── main.py
├── requirements.txt
└── README.md

Installation & Setup

1. Clone the repo

git clone <your-repo-link>
cd fake-news-detection

2. Install dependencies

pip install -r requirements.txt

3. Add the dataset

Grab Fake.csv and True.csv, then drop them into the data/ folder.

Usage

Just run:

python main.py

You’ll see something like:

Accuracy: 0.98
Enter news text:

Type in your news article, and the model spits back:

Prediction: Real News / Fake News

Results

- Model Accuracy: about 98%
- Finds fake and real news using text patterns

Limitations

- Only checks for text patterns, doesn’t fact-check
- Short or vague entries can fool it
- Quality of predictions depends on the dataset

Future Improvements

- Build a web interface with Streamlit
- Use stronger NLP models like BERT
- Train on bigger datasets for better accuracy
- Turn it into a full web app


Author
Prince Agrawal

Conclusion
This project shows how AI and NLP can help with real-world headaches like fake news. It puts the spotlight on smart preprocessing, feature extraction, and picking the right model—key steps for creating solid AI systems.