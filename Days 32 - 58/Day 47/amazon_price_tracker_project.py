from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
load_dotenv()

from_address = os.environ.get("SMTP_ADDRESS")
to_address = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")

TARGET_PRICE = 100.00
#URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/138.0.0.0 Safari/537.36")

accept_language = "en-GB,en-US;q=0.9,en;q=0.8"

headers = {"User-Agent": user_agent,
           "Accept-Language": accept_language}

response = requests.get(URL, headers=headers)
content = response.text

soup = BeautifulSoup(content, "html.parser")
whole_number = soup.find(name = "span", class_ = "aok-offscreen")

current_price = ""
for item in whole_number:
    #current_price = float(item.getText().split("$")[1])
    current_price = float(item.getText().split("with")[0].strip().split("$")[1])

email_message = f"{' '.join(soup.find(id = 'productTitle').getText().split())} is now ${current_price}!"

if current_price < TARGET_PRICE:
    print(email_message)
