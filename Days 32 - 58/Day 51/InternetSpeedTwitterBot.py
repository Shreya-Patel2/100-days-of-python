from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = "###"
TWITTER_PASSWORD = "###"
TWITTER_EMAIL = "###"

OS = os.name

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
if OS == "nt":
    chrome_options.add_argument(
        r'--user-data-dir=###')

chrome_options.add_argument('--disable-blink-features=AutomationControlled')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        go = self.driver.find_element(By.XPATH,
                                      value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')
        go.click()
        time.sleep(40)
        download = self.driver.find_element(By.XPATH,
                                            value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        upload = self.driver.find_element(By.XPATH,
                                          value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(f"Down: {download.text}\nUp: {upload.text}")

    def tweet_at_provider(self):
        time.sleep(2)
        sign_in = self.driver.find_element(By.XPATH,
                                           value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[2]/div[3]/a/div/span/span')
        sign_in.click()
        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
