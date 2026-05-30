import pandas as pd

def basic_stats(df, title):
    """
    Prints basic dataframe statistics.

    Includes:
    - shape
    - column names
    - data types
    - missing values
    - duplicate rows
    - first rows

    :param df: dataframe to inspect.
    :param title: title displayed above the statistics output.
    """
    print(f"\n === {title} ===")

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(list(df.columns))

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nDuplicated rows:")
    print(df.duplicated().sum())

    print("\nFirst rows:")
    print(df.head())

def compare_stats(raw_df, clean_df):
    """
    Prints a comparison between raw and clean datasets.

    Includes:
    - row count before and after cleaning
    - number of removed rows
    - column count comparison
    - missing values before and after cleaning
    - duplicate rows before and after cleaning

    :param raw_df: original raw data
    :param clean_df: cleaned dataframe.
    """
    print(f"\n === Cleaning Summary ===")

    print(f"Rows BEFORE cleaning: {len(raw_df)}")
    print(f"Rows AFTER cleaning: {len(clean_df)}")
    print(f"TOTAL removed: {len(raw_df) - len(clean_df)}")

    print(f"\nColumns BEFORE cleaning: {len(raw_df.columns)}")
    print(f"Columns AFTER cleaning: {len(clean_df.columns)}")

    print("\nMissing values BEFORE:")
    print(raw_df.isna().sum())
    print("\nMissing values AFTER:")
    print(clean_df.isna().sum())

    print("\nDuplicated rows BEFORE:")
    print(raw_df.duplicated().sum())
    print("\nDuplicated rows AFTER:")
    print(clean_df.duplicated().sum())
