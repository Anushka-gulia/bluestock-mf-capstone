import pandas as pd
from pathlib import Path

# Project root directory
project_root = Path(__file__).resolve().parent.parent

# Raw data folder
data_folder = project_root / "data" / "raw"

# List of datasets
datasets = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 80)
print("BLUESTOCK MUTUAL FUND ANALYTICS")
print("DATA INGESTION REPORT")
print("=" * 80)

for file_name in datasets:
    try:
        file_path = data_folder / file_name

        print(f"\n{'='*80}")
        print(f"DATASET: {file_name}")
        print(f"{'='*80}")

        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nDataset Loaded Successfully")

    except Exception as e:
        print(f"\nError loading {file_name}")
        print(f"Reason: {e}")

print("\n")
print("=" * 80)
print("ALL DATASETS PROCESSED")
print("=" * 80)