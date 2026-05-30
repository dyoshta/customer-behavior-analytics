from cleaning.preprocessing import normalize_column_names, remove_duplicates, handle_missing, remove_invalid_rows, \
    fix_datatypes, add_total_price

def run_cleaning(df):
    """
    Executes the complete data cleaning pipeline.

    Current steps:
    1. Normalize column names;
    2. Remove duplicates;
    3. Remove rows with missing customer_id value;
    4. Remove rows with invalid transactions (quantity <= 0 & unit_price <= 0)
    5. Fix datatypes
    6. Add a total_price column

    :param df: raw dataframe.
    :return: cleaned dataframe (df).
    """
    df = normalize_column_names(df)
    df = remove_duplicates(df)
    df = handle_missing(df)
    df = remove_invalid_rows(df)
    df = fix_datatypes(df)
    df = add_total_price(df)
    return df

