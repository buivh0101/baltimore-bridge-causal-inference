import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CENSUS_API_KEY")

ports = {
    "Baltimore": "1303",
    "Norfolk": "1401",
    "Charleston": "1601",
    "Savannah": "1703",
    "Houston": "5301",
    "Jacksonville": "1803",
    "New Orleans": "2002",
    "Oakland": "2811",
    "Boston": "0401",
    "Brunswick": "1701",
    "Tampa": "1801",
    "Port Canaveral": "1816",
    "Port Everglades": "5203",
    "Corpus Christi": "5312",
    "Seattle": "3001",
    "Tacoma": "3002",
    "Portland OR": "2904"
}

url = "https://api.census.gov/data/timeseries/intltrade/imports/porths"

all_data = []

for name, code in ports.items():

    params = {
        "get": "VES_VAL_MO,VES_WGT_MO,PORT_NAME",
        "time": "from 2019-01 to 2026-07",
        "PORT": code,
        "key": api_key
    }

    data = requests.get(url, params=params).json()

    temp = pd.DataFrame(data[1:], columns=data[0])
    temp["port"] = name

    all_data.append(temp)

    print("Done:", name)

df = pd.concat(all_data, ignore_index=True)

df.to_csv("data/raw/all_ports_imports.csv", index=False)

print(df.shape)