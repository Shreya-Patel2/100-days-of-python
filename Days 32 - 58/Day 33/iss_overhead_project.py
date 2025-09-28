import requests
from datetime import datetime

MY_LAT = 00.000000  # Your latitude
MY_LONG = 00.000000  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
lat_range = [MY_LAT + num for num in range(-5, 6)]
long_range = [MY_LONG + num for num in range(-5, 6)]

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if sunrise <= time_now.hour <= sunset:
    if iss_latitude in lat_range and iss_longitude in long_range:
        print("Go look up!")
