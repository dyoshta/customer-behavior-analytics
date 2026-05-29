

def normalize_column_names(df):
    """
    Renames raw dataset columns to snake_case format.

    :param df: raw dataframe with original column names.
    :return: dataframe with normalized column names (df).
    """
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
    """
    Removes fully duplicated rows from the dataframe.

    :param df: input dataframe.
    :return: dataframe without duplicate rows.
    """
    return df.drop_duplicates()

def handle_missing(df):
    """
    Removes rows without customer_id.

    Rows without customer_id are removed, because customer-level analysis
    requires a valid customer identifier.

    :param df: input dataframe.
    :return: dataframe without missing customer_id values.
    """
    return df.dropna(subset=["customer_id"])

# TODO: def remove_invalid_rows(df):

