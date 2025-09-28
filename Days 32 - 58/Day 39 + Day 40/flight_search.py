import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    pass


# ------------------------------------------- DATES / AMADEUS API ------------------------------------------------------

TOMORROW = (datetime.now() + relativedelta(days=1)).strftime("%Y-%m-%d")
SIX_MONTHS_AHEAD = (datetime.now() + relativedelta(months=6)).strftime("%Y-%m-%d")
API_KEY = "###"
API_Secret = "###"

# ------------------------------------------- OBTAIN AMADEUS TOKEN -----------------------------------------------------

header = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_Secret}

response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=data)
info = response.json()["access_token"]
TOKEN = f"Bearer {info}"

# -----------------------------------  GET LIST OF CITIES IN GOOGLE SHEET ----------------------------------------------

headers_sheetly = {"Authorization": "###",
                   "Content-Type": "application/json"}

update = requests.get(url="https://api.sheety.co/66e59e57b590a482ec94f5db846d6cc9/flightDeals/prices",
                      headers=headers_sheetly)
rows = update.json()["prices"]
city_list = [(rows[num]["city"]).upper() for num in range(0, len(rows))]

# --------------------------------  GET LIST OF CITY CODES FOR CITIES IN CITY LIST -------------------------------------

header = {"Authorization": TOKEN}
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

# --------------------------------------  UPDATE GOOGLE SHEET WITH CODES -----------------------------------------------

body = [0, 0]
for num in range(0, len(city_list)):
    row_body = {"price": {"code": CITY_CODES[num]}}
    body.append(row_body)

for item in range(2, 8):
    response = requests.put(url=f"https://api.sheety.co/66e59e57b590a482ec94f5db846d6cc9/flightDeals/prices/{item}",
                            headers=headers_sheetly, json=body[item])
print(response.json())

# ----------------------------------  SEARCH FOR FIGHTS AND GENERATE ALERTS --------------------------------------------

parameters_flight = []
for num in range(0, len(CITY_CODES)):
    parameters = {"originLocationCode": "LON",
                  "destinationLocationCode": CITY_CODES[num],
                  "departureDate": TOMORROW,
                  "returnDate": SIX_MONTHS_AHEAD,
                  "adults": 1,
                  "maxPrice": 300}
    parameters_flight.append(parameters)

notifications = []
for num in range(0, len(CITY_CODES)):
    response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=parameters_flight[num],
                            headers=header)
    flight_options = response.json()["data"]
    number_of_flights = len(flight_options)

    for num in range(0, number_of_flights):
        code_depart = flight_options[num]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        depart = flight_options[num]["itineraries"][0]["segments"][0]["departure"]["at"]
        code_arrive = flight_options[num]["itineraries"][1]["segments"][0]["departure"]["iataCode"]
        arrive = flight_options[num]["itineraries"][1]["segments"][0]["departure"]["at"]
        price = flight_options[num]["price"]["grandTotal"]
        depart_date = depart.split("T")[0]
        arrive_date = arrive.split("T")[0]

        alert = f"Low price alert! Only £{price} to fly from {code_depart} to {code_arrive}, on {depart_date} until {arrive_date}."
        if alert not in notifications:
            notifications.append(alert)

print(notifications)
