import pandas as pd

from config import RAW_DATA_PATH

def load_raw_data():
    df = pd.read_excel(RAW_DATA_PATH)
    return df

def inspect_data(df):
    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nDuplicated rows:")
    print(df.duplicated().sum())

    print("\nFirst rows:")
    print(df.head())

def run_cleaning():
    df = load_raw_data()
    inspect_data(df)