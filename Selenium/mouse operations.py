from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

# Open the jQuery UI Menu page
driver.get("https://jqueryui.com/menu/")
driver.maximize_window()

# Switch to the iframe (Menu is inside an iframe)
driver.switch_to.frame(0)

# Explicit wait to ensure menu elements are loaded
wait = WebDriverWait(driver, 10)

# Locate the "Electronics" menu item
electronics = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='ui-id-4']")))

# Perform mouse hover over "Electronics" to display the "Car" submenu
act = ActionChains(driver)
act.move_to_element(electronics).perform()

# Wait for "Car" submenu to become visible
car = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='ui-id-6']")))

# Hover over "Car" and click it
act.move_to_element(car).click().perform()

# Wait to observe the result
time.sleep(5)

# Close the browser
driver.quit()