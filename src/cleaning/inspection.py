
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

def inspect_invalid_rows(df):
    print("\nRows with quantity <= 0:")
    print((df["quantity"] <= 0).sum())
    print("\nRows with unit price <= 0:")
    print((df["price"] <= 0).sum())