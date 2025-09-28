from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"
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

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("###")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("###")
email_name = driver.find_element(By.NAME, value="email")
email_name.send_keys("###", Keys.ENTER)


