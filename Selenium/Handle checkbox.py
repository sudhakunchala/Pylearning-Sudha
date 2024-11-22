from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

obj_ser=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj_ser)

driver.get("https://demoqa.com/checkbox")
driver.maximize_window()

# finding one checkbox
driver.find_element(By.XPATH,"")