from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


URL = "https://www.facebook.com/"
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

email = driver.find_element(By.ID, value="email")
email.send_keys("###")

password = driver.find_element(By.ID, value="pass")
password.send_keys("###")
password.send_keys(Keys.ENTER)

search = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/label/input')
search.send_keys("Sky News", Keys.ENTER)
wait = WebDriverWait(driver, 15)


body = driver.find_element(By.TAG_NAME, 'body')
for num in range(3):
    body.send_keys(Keys.END)
    time.sleep(2)

like_buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Like']")
for button in like_buttons:
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)  # Small pause after scrolling

    # Use WebDriverWait to ensure the button is clickable before clicking

    clickable_button = wait.until(EC.element_to_be_clickable(button))
    clickable_button.click()