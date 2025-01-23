import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

#if you see authentication popup ,then we can handle this with sending userid and pwd through URL itself
# syntax: https://username:password@test.com

#driver.get("https://the-internet.herokuapp.com/basic_auth") # This is the real url
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth") #This is injected username and pwd
driver.maximize_window()
time.sleep(5)

driver.close()