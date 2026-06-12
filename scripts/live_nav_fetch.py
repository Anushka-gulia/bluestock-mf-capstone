import requests
import pandas as pd
from pathlib import Path

# HDFC Top 100 Direct Fund
scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    output_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "hdfc_top100_live_nav.csv"

    nav_df.to_csv(output_path, index=False)

    print("NAV data fetched successfully")
    print(f"Records fetched: {len(nav_df)}")
    print(f"Saved to: {output_path}")

except Exception as e:
    print("Error:", e)