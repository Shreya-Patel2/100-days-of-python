from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4215346420&distance=25.0&geoId=102257491&keywords=python%20developer&origin=HISTORY"
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

time.sleep(5)

sign_in = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
username = driver.find_element(By.ID, value="username")
username.send_keys("###")
password = driver.find_element(By.ID, value="password")
password.send_keys("###")
login = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[4]/button')
login.click()

easy_apply = driver.find_element(By.ID, value="searchFilter_applyWithLinkedin")
easy_apply.click()
time.sleep(2)

jobs = driver.find_elements(By.CSS_SELECTOR, value="span:nth-child(1) > strong")
for item in jobs:
    item.click()
    time.sleep(1)
    save = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button/span[1]')
    save.click()
    time.sleep(2)

