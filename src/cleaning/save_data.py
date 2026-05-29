from config import PROCESSED_DATA_PATH

def save_clean_data(df):
    """
    Saves the cleaned dataset as CSV file.

    The file is saved to the processed data directory defined in config.py.

    :param df: cleaned dataframe to save.
    """
    df.to_csv(PROCESSED_DATA_PATH, index=False)