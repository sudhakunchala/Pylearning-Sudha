from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://facebook.com/")
driver.maximize_window()

#driver.find_element(By.ID,"email").send_keys("sudha2320@gmail.com ")  # this is about id locator


input("Please enter to close the browser...")
driver.quit()