from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#driver.save_screenshot("C:/Users/sudha/Desktop/screen.png") # we need give the path where we save the screenshot along with the name of the screenshot
driver.save_screenshot(os.getcwd()+"screen1.png") #os.getcwd() can use instead of path, it will save in the current directory
time.sleep(5)

driver.quit()
