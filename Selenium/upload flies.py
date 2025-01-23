from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.file.io/")
driver.maximize_window()

driver.find_element(By.XPATH,"//label[normalize-space()='Upload Files']").send_keys("C:/Users/sudha/Desktop/akki worksheets/abc-connect-the-dots.pdf")