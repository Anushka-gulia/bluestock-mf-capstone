import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

processed_path = BASE_DIR / "data" / "processed"
db_path = BASE_DIR / "data" / "db" / "mutual_fund.db"

# Load cleaned datasets
fund_master = pd.read_csv(
    processed_path / "fund_master_clean.csv"
)

nav_history = pd.read_csv(
    processed_path / "nav_history_clean.csv"
)

transactions = pd.read_csv(
    processed_path / "transactions_clean.csv"
)

# Create SQLite database
conn = sqlite3.connect(db_path)

fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "transactions",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("Database created successfully!")
print(f"Saved at: {db_path}")