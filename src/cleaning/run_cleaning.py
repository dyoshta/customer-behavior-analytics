from cleaning.preprocessing import normalize_column_names, remove_duplicates, handle_missing
from config import PROCESSED_DATA_PATH


def run_cleaning(df):
    """
    Executes the complete data cleaning pipeline.

    Current steps:
    1. Normalize column names;
    2. Remove duplicates;
    3. Remove rows with missing customer_id value;

    :param df: raw dataframe.
    :return: cleaned dataframe (df).
    """
    df = normalize_column_names(df)
    df = remove_duplicates(df)
    df = handle_missing(df)
    return df

