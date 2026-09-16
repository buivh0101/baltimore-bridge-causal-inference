import os
import requests
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

# Load API key
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("CENSUS_API_KEY", "").strip()

url = "https://api.census.gov/data/timeseries/intltrade/imports/porths"

months = pd.date_range(
    start="2019-01-01",
    end="2026-08-01",
    freq="MS"
)

rows = []

for month in months:

    month_text = month.strftime("%Y-%m")

    params = {
        "get": "GEN_VAL_MO,VES_VAL_MO,VES_WGT_MO,PORT_NAME",
        "time": month_text,
        "PORT": "1303",
        "key": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200 and response.text.strip():
        data = response.json()

        if len(data) > 1:
            rows.append(data[1])
            print("Downloaded:", month_text)

columns = [
    "general_import_value",
    "vessel_import_value",
    "vessel_import_weight",
    "port_name",
    "month",
    "port_code"
]

df = pd.DataFrame(rows, columns=columns)

output_path = Path("data/raw/baltimore_imports.csv")

df.to_csv(output_path, index=False)

print("\nSaved:", output_path)
print("Rows:", len(df))