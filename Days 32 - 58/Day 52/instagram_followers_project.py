from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from InstaFollower import InstaFollower

URL = "https://www.instagram.com/"

bot = InstaFollower()
bot.driver.get(URL)
bot.login()
bot.find_followers()
bot.follow()