from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()

#driver.find_element(By.LINK_TEXT,"Register").click()

# If you want open register in new tab, below is the way
# reglink=Keys.CONTROL+Keys.ENTER
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)
# time.sleep(5)

# # In Selenium 4 introduced new_window: opens a new tab and switches to new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com/")

# In Selenium 4 introduced new_window: opens a new window and switches to new browser
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")



driver.quit()