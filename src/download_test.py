import os
import requests
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("CENSUS_API_KEY")

print("API key loaded:", api_key is not None)

url = "https://api.census.gov/data/timeseries/intltrade/imports/porths"

params = {
    "get": "GEN_VAL_MO,VES_VAL_MO,VES_WGT_MO,PORT_NAME",
    "time": "2024-01",
    "PORT": "1303",
    "key": api_key
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.text)