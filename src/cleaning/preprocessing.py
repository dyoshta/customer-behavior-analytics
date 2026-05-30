import pandas as pd


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

def remove_invalid_rows(df):
    """
    Removes rows containing invalid transaction values.

    Rows with non-positive quantity or unit_price are removed
    because they do not represent valid sales transactions.

    :param df: input dataframe.
    :return: dataframe containing only valid transactions.
    """
    return df[
        (df["quantity"] > 0) &
        (df["unit_price"] > 0)
    ]
def fix_datatypes(df):
    """
    Explicitly converts dataframe columns to expected data types.

    :param df: input dataframe.
    :return: dataframe with corrected data types.
    """
    df = df.copy()

    df["invoice_no"] = df["invoice_no"].astype(str)
    df["stock_code"] = df["stock_code"].astype(str)
    df["description"] = df["description"].astype(str)
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].astype(float)
    df["customer_id"] = df["customer_id"].astype(int)
    df["country"] = df["country"].astype(str)

    df["invoice_date"] = pd.to_datetime(df["invoice_date"])

    return df


# TODO def add_total_price(df):

