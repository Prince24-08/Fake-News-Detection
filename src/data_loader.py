import pandas as pd

def load_data():
    fake = pd.read_csv("data/Fake.csv")
    real = pd.read_csv("data/True.csv")

    fake["label"] = 0
    real["label"] = 1

    data = pd.concat([fake, real])
    data = data.sample(frac=1).reset_index(drop=True)

    return data