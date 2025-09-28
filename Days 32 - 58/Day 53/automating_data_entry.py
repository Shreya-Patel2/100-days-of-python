from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

FORM_LINK = "###"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_LINK)
content = response.text

soup = BeautifulSoup(content, "html.parser")
links = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
addresses = soup.find_all(name="address")

listing_links = [link.get("href") for link in links]
listing_prices = [(str(price.getText)).split("property-card-price")[1].split("/")[0].split("+")[0].split(">")[1] for price in prices]
listing_addresses = [(str(address.getText)).split("property-card-addr")[1].split(">")[1].strip().split("<")[0].strip() for address in addresses]

print(listing_addresses)

headers_sheetly = {"Authorization": "###",
                   "Content-Type": "application/json"}


body = []
for num in range(0, len(listing_addresses)):
    row_body = {"sheet1": {"address": listing_addresses[num],
                           "price": listing_prices[num],
                           "link": listing_links[num]}}
    body.append(row_body)

for item in range(0,len(listing_addresses)):
    response = requests.post(url=f"###", headers=headers_sheetly, json=body[item])
print(response.json())
