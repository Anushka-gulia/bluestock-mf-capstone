import pandas as pd
from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

raw_path = BASE_DIR / "data" / "raw"
processed_path = BASE_DIR / "data" / "processed"

# Create processed folder if it doesn't exist
processed_path.mkdir(exist_ok=True)

# ==========================
# LOAD DATASETS
# ==========================

fund_master = pd.read_csv(
    raw_path / "01_fund_master.csv"
)

nav_history = pd.read_csv(
    raw_path / "02_nav_history.csv"
)

transactions = pd.read_csv(
    raw_path / "08_investor_transactions.csv"
)

# ==========================
# FUND MASTER CLEANING
# ==========================

fund_master.drop_duplicates(inplace=True)

if "launch_date" in fund_master.columns:
    fund_master["launch_date"] = pd.to_datetime(
        fund_master["launch_date"],
        errors="coerce"
    )

# ==========================
# NAV HISTORY CLEANING
# ==========================

nav_history.drop_duplicates(inplace=True)

if "date" in nav_history.columns:
    nav_history["date"] = pd.to_datetime(
        nav_history["date"],
        errors="coerce"
    )

if "nav" in nav_history.columns:
    nav_history["nav"] = pd.to_numeric(
        nav_history["nav"],
        errors="coerce"
    )

# ==========================
# TRANSACTIONS CLEANING
# ==========================

transactions.drop_duplicates(inplace=True)

if "transaction_date" in transactions.columns:
    transactions["transaction_date"] = pd.to_datetime(
        transactions["transaction_date"],
        errors="coerce"
    )

if "amount_inr" in transactions.columns:
    transactions["amount_inr"] = pd.to_numeric(
        transactions["amount_inr"],
        errors="coerce"
    )

# Fill missing values safely

if "city" in transactions.columns:
    transactions["city"] = transactions["city"].fillna("Unknown")

if "state" in transactions.columns:
    transactions["state"] = transactions["state"].fillna("Unknown")

# ==========================
# SAVE CLEAN DATA
# ==========================

fund_master.to_csv(
    processed_path / "fund_master_clean.csv",
    index=False
)

nav_history.to_csv(
    processed_path / "nav_history_clean.csv",
    index=False
)

transactions.to_csv(
    processed_path / "transactions_clean.csv",
    index=False
)

# ==========================
# SUMMARY
# ==========================

print("\nDATA CLEANING COMPLETED SUCCESSFULLY\n")

print("Fund Master Records :", len(fund_master))
print("NAV History Records :", len(nav_history))
print("Transaction Records :", len(transactions))

print("\nFiles saved to:")
print(processed_path)