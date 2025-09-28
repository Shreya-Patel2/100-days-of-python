import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

TOMORROW = (datetime.now() + relativedelta(days=1)).strftime("%Y-%m-%d")
SIX_MONTHS_AHEAD = (datetime.now() + relativedelta(months=6)).strftime("%Y-%m-%d")
API_KEY = "###"
API_Secret = "###"

header = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_Secret}

response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=data)
info = response.json()["access_token"]

TOKEN = f"Bearer {info}"

header = {"Authorization": TOKEN}

headers_sheetly = {"Authorization": "###",
                   "Content-Type": "application/json"}

update = requests.get(url="###",
                      headers=headers_sheetly)
rows = update.json()["prices"]

city_list = [(rows[num]["city"]).upper() for num in range(0, len(rows))]

parameters = []
for num in range(0, len(city_list)):
    parameters_city = {"subType": "CITY",
                       "keyword": city_list[num]}
    parameters.append(parameters_city)

CITY_CODES = []
for num in range(0, len(city_list)):
    response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations", params=parameters[num],
                            headers=header)
    codes = response.json()["data"][0]["address"]["cityCode"]
    CITY_CODES.append(codes)
# print(CITY_CODES)


body = [0, 0]
for num in range(0, len(city_list)):
    row_body = {"price": {"code": CITY_CODES[num]}}
    body.append(row_body)

for item in range(2, 8):
    response = requests.put(url=f"https://api.sheety.co/66e59e57b590a482ec94f5db846d6cc9/flightDeals/prices/{item}",
                            headers=headers_sheetly, json=body[item])
print(response.json())
