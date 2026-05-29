import sys

from cleaning.load_data import load_raw_data, load_clean_data
from cleaning.run_cleaning import run_cleaning
from cleaning.save_data import save_clean_data
from cleaning.statistics import basic_stats, compare_stats


def main():
    if len(sys.argv) == 1:
        raw_df = load_raw_data()
        clean_df = run_cleaning(raw_df)
        save_clean_data(clean_df)
        print("Cleaned data saved successfully.")
        return

    command = sys.argv[1]

    if command == "raw-stats":
        raw_df = load_raw_data()
        basic_stats(raw_df, "Raw Data Statistics")

    elif command == "cleaned-stats":
        clean_df = load_clean_data()
        basic_stats(clean_df, "Cleaned Data Statistics")

    elif command == "compare-stats":
        raw_df = load_raw_data()
        clean_df = load_clean_data()
        compare_stats(raw_df, clean_df)

    else:
        print(f"Unknown command: {command}")
        print("Choose among available commands: ")
        print("\nraw-stats")
        print("\ncleaned-stats")
        print("\ncompare-stats")

if __name__ == "__main__":
    main()