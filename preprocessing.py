import pandas as pd

def preprocess(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.fillna(0)
    return df
