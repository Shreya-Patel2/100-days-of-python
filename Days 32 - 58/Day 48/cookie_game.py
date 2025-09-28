from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time

URL = 'https://ozh.github.io/cookieclicker/'
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

clicker = driver.find_element(By.ID, value="bigCookie")
t_end = time.time() + 10
while time.time() < t_end:
    clicker.click()

driver.quit()