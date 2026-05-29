import pandas as pd

from config import RAW_DATA_PATH, PROCESSED_DATA_PATH


def load_raw_data():
    """
    Loads the raw Online Retail dataset from the Excel file.

    :return: raw dataset loaded from the source file (df).
    """
    return pd.read_excel(RAW_DATA_PATH)


def load_clean_data():
    """
    Loads the cleaned dataset from the processed CSV file.

    :return: cleaned dataset loaded from the processed file (df).
    """
    return pd.read_csv(PROCESSED_DATA_PATH)
