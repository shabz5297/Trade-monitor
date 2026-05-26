import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("COMTRADE_API_KEY")

url = "https://comtradeapi.un.org/data/v1/get/C/A/HS"

headers = {"Ocp-Apim-Subscription-Key": API_KEY}

params = {
    "reporterCode": "826",   # UK
    "partnerCode": "156",    # China
    "flowCode": "M",         # Imports
    "cmdCode": "TOTAL",
    "period": "2024" }

response = requests.get(url, headers=headers, params=params)

print("STATUS:", response.status_code)

data = response.json()
records = data.get("data", [])

for record in records[:5]:
    print("----------------")
    print("Reporter:", record.get("reporterDesc"))
    print("Partner:", record.get("partnerDesc"))
    print("Trade Value:", record.get("primaryValue"))
    print("Commodity:", record.get("cmdDesc"))

print(json.dumps(data, indent=2))
