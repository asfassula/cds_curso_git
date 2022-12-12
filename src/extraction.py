import pandas as pd


def load_data():
    return pd.read.csv ('data/processed/bikes_completed.csv')
