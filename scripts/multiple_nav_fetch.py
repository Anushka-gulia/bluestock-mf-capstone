import requests
import pandas as pd
from pathlib import Path

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

output_folder = Path(__file__).resolve().parent.parent / "data" / "raw"

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = output_folder / f"{fund_name}_nav.csv"

        nav_df.to_csv(file_path, index=False)

        print(f"{fund_name} downloaded successfully")

    except Exception as e:
        print(f"Error downloading {fund_name}: {e}")