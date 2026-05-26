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

def normalize_column_names(df):
    df = df.rename(columns={
        "InvoiceNo": "invoice_no",
        "StockCode": "stock_code",
        "Description": "description",
        "Quantity": "quantity",
        "InvoiceDate": "invoice_date",
        "UnitPrice": "unit_price",
        "CustomerID": "customer_id",
        "Country": "country"
    })
    return df

def remove_duplicates(df):
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"Removed duplicate rows: {before - after}")
    return df

def handle_missing(df):
    print("Missing values before: ")
    print(df.isna().sum())
    before = len(df)

    df = df.dropna(
        subset=["customer_id"]
    )

    after = len(df)
    print(f"\nRemoved rows with missing customer_id: {before - after}")
    print("\nMissing values AFTER: ")
    print(df.isna().sum())
    return df



def run_cleaning():
    print("Loading raw data...")
    df = load_raw_data()

    print("Raw data overview:")
    inspect_data(df)

    print("Normalizing column names...")
    df = normalize_column_names(df)

    print("Column names after normalization:")
    print(list(df.columns))

    print("Removing duplicates...")
    df = remove_duplicates(df)

    print("Shape after removing duplicates:")
    print(df.shape)

    print("Handling missing values...")
    df = handle_missing(df)

    print("Shape after missing values:")
    print(df.shape)
