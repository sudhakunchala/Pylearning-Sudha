#close()
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://www.amazon.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Holiday Deals").click()
input("press enter to close the app..")

driver.close()

