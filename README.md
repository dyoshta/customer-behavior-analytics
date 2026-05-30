# Customer Behavior Analytics
## Project Overview

This project is an end-to-end data analytics portfolio project based on an e-commerce dataset.

The goal is to build a complete analytics pipeline:

1. Load raw data
2. Clean and preprocess data with Python
3. Prepare data for PostgreSQL analysis
4. Build SQL queries
5. Create a Power BI dashboard
6. Summarize business insights

## Dataset

Source:
Online Retail Dataset (UCI Machine Learning Repository)

The dataset contains transactional e-commerce data including:

- invoices
- products
- quantities
- prices
- customer identifiers
- countries
- transaction timestamps

## Technologies

- Python
- pandas
- PostgreSQL (planned)
- SQL (planned)
- Power BI (planned)
- Git / GitHub

## Current Project Status
Current version includes the first Python cleaning pipeline.
Implemented steps:

- loading raw Excel dataset
- normalizing column names
- removing duplicated rows
- removing rows with missing `customer_id`
- saving cleaned data as CSV
- basic raw/cleaned statistics commands

## Project Structure
```text
customer-behavior-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── main.py
│   ├── config.py
│   └── cleaning/
│       ├── __init__.py
│       ├── load_data.py
│       ├── preprocessing.py
│       ├── run_cleaning.py
│       ├── save_data.py
│       └── statistics.py
│
├── requirements.txt
└── README.md
```

## How to Run
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the default cleaning pipeline:
```bash
python src/main.py
```
Show raw dataset statistics:
```bash
python src/main.py raw-stats
```
Show cleaned dataset statistics:
```bash
python src/main.py cleaned-stats
```
Compare raw and clean datasets:
```bash
python src/main.py compare-stats
```

## Current Cleaning Steps
1. Rename columns to snake_case
2. Remove fully duplicated rows
3. Remove rows with missing `customer_id`
4. Remove invalid rows where quantity <= 0 or unit_price <= 0
5. Convert columns to expected data types
6. Add total_price column
7. Save cleaned dataset to data/processed/

## Next Steps
- load cleaned data into PostgreSQL
- write SQL analytics queries
- build Power BI dashboard