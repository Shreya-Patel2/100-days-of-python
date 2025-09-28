from selenium import webdriver
import os
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"
OS = os.name

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Option to keep Chrome open
chrome_options.add_experimental_option("excludeSwitches", [
    "enable-automation"])  # Remove the Chrome infobar - "Chrome controlled by automated test software"
if OS == "nt":
    # Windows
    chrome_options.add_argument(
        r'--user-data-dir=###')  # Specify path to the new user I have called SeleniumProfile

chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # Prevent Selenium being detected as a bot
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

number= ["1", "2", "3", "4", "5"]
events_dict = {}

for num in number:
    all_events = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{num}]/time')
    event_names = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{num}]/a')
    dict_item = {num:{all_events.text:event_names.text}}
    events_dict.update(dict_item)


print(events_dict)
driver.quit()
