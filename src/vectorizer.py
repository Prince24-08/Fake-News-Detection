from sklearn.feature_extraction.text import TfidfVectorizer

def get_vectorizer():
    return TfidfVectorizer(stop_words="english", max_df=0.7, ngram_range=(1,2))