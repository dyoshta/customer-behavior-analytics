from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "online_retail.xlsx"
PROCESSED_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    /"online_retail_cleaned.csv"
)