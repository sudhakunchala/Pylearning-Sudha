from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#To handle notification popup we need to add 
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj,options=ops)




driver.get("https://whatmylocation.com/")
driver.maximize_window()

driver.quit();