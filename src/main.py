
from cleaning.inspection import inspect_data, inspect_invalid_rows
from cleaning.load_data import load_raw_data
from cleaning.preprocessing import normalize_column_names, remove_duplicates, handle_missing

if __name__ == "__main__":
    df = load_raw_data()
    inspect_data(df)
    df = normalize_column_names(df)
    df = remove_duplicates(df)
    df = handle_missing(df)
    inspect_invalid_rows(df)
    df = remove_invalid_rows(df) #TODO
    df = add_total_price(df) #TODO
    save_cleaned_data(df) #TODO