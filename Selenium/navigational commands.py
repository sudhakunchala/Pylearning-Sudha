from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser_obj=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.get("https://www.macys.com/")


driver.back()
driver.forward()

driver.refresh()

input("press enter to close the app..")
driver.quit()