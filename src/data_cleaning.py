import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df = df.drop_duplicates()

    numeric_columns = ["temperature","hour","population","growth_rate","capacity"]
    # "10" to 10, if a value cannot be converted change to NaN
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric,erros = "coerse")
    # population cannot be negative and makes no sense to have an capacity lower than zero
    df = df[df["population"] >= 0]
    df = df[df["capacity"] > 0]
    df = df.dropna()

    return df