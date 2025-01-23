from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

# Open the URL
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.maximize_window()

# Click on the link to open a new window
driver.find_element(By.LINK_TEXT, "Privacy Policy").click()

# Wait for new window to open
time.sleep(2)

# Get window handles
windowsIDs = driver.window_handles

# Store parent and child window IDs
parent_window_id = windowsIDs[0]
child_window_id = windowsIDs[1]

# Switch to the child window
driver.switch_to.window(child_window_id)
print("Child Window Title:", driver.title)

# Switch back to the parent window
driver.switch_to.window(parent_window_id)
print("Parent Window Title:", driver.title)

# Cleanup - close all windows
driver.quit()