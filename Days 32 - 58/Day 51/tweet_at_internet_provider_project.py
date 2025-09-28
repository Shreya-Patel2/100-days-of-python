from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

# PROMISED_DOWN = 150
# PROMISED_UP = 10
# CHROME_DRIVER_PATH = "###"

TWITTER_URL = "https://x.com/"
SPEED_TEST_URL = "https://www.speedtest.net/"

# URL =
# driver.get(URL)

InternetSpeedTwitterBot = InternetSpeedTwitterBot()
InternetSpeedTwitterBot.driver.get(SPEED_TEST_URL)
# InternetSpeedTwitterBot.get_internet_speed()

InternetSpeedTwitterBot.driver.get(TWITTER_URL)
InternetSpeedTwitterBot.tweet_at_provider()


