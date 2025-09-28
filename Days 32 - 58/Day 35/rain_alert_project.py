import requests

api_key = "###"
lon = "###"
lat = "###"
hours = "4"

parameters = {"lat": lat, "lon": lon, "appid": api_key, "cnt":hours}

forecast = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = forecast.json()
ID = [data["list"][num]["weather"][0]["id"] for num in range(0,4)]
if ID[0] or ID[1] or ID[2] or ID[3] < 700:
    print("Bring an umbrella")