from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Use the Select class for dropdowns

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

# Open the website
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# Locate the dropdown and select an option
drpcountry = driver.find_element(By.XPATH, "//select[@id='input-country']")
drpcountry.select_by_visible_text("India")  # Select option by visible text

# Close the browser
input("press enter to close the app..")
driver.quit()


