

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