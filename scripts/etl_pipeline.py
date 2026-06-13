import os

print("Starting ETL Pipeline")

os.system("python scripts/data_ingestion.py")
os.system("python scripts/data_cleaning.py")
os.system("python scripts/create_database.py")

print("ETL Completed Successfully")