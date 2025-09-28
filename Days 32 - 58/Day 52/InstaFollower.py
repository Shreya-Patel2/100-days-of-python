from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

DECLINE_COOKIES = '//*[@id="mount_0_0_38"]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/div/div/div'
SIMILAR_ACCOUNT = "###"
USERNAME = "###"
PASSWORD = "###"

OS = os.name

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
if OS == "nt":
    chrome_options.add_argument(
        r'--user-data-dir=###')

chrome_options.add_argument('--disable-blink-features=AutomationControlled')


class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(2)
        # save_info_button = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Not now')]")
        # save_info_button.click()
        # time.sleep(2)
        #
        # cookie_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Decline otional cookies')]")
        # cookie_button.click()
        save_info_button = self.driver.find_element(By.XPATH,
                                                    value='//*[@id="mount_0_0_tU"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div')
        save_info_button.click()
        cookie_button = self.driver.find_element(by=By.XPATH, value=DECLINE_COOKIES)
        cookie_button.click()

    def find_followers(self):
        print("find followers")

    def follow(self):
        print("follow")
