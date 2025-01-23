import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# this will find the web element and do click
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

# Next popup alert will open up
# alert is not a web element
# to handle alert we use switch_to.alert command

alertwindow=driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")

# to say ok ,we use accept()
# to cancel the alert ,we use dismiss()

#alertwindow.accept() # this will close the alert window by clicking Ok

alertwindow.dismiss() # this will close the alert window by clicking cancel button
