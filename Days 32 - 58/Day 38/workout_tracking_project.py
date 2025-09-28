import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETLY_TOKEN = os.environ["SHEETLY_TOKEN"]

headers = {"Content-Type": "application/json",
           "x-app-id": APP_ID,
           "x-app-key": API_KEY}

query = input("What exercise did you do?")

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json={"query": query})
data = response.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
exercise = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

body = {"workout": {"date": date,
                     "time": time,
                     "exercise": exercise,
                     "duration": duration,
                     "calories": calories}}

headers_sheetly = {"Authorization": "###",
                   "Content-Type": "application/json",
                   "x-app-id": APP_ID,
                   "x-app-key": API_KEY}

update = requests.post(url="###", headers=headers_sheetly, json=body)
print(update.text)

