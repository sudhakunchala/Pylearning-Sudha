from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# Switch to the frame (datepicker is inside an iframe)
driver.switch_to.frame(0)

# Input data
year = "2023"
month = "April"
date = "9"

# Open the datepicker
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

# Navigate to the desired month and year
while True:
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if current_month == month and current_year == year:
        break
    else:
        # Navigate to the previous month (use next if needed)
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()  # Click on the previous arrow

time.sleep(2)  # Wait for navigation to complete

# Select the desired date
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for d in dates:
    if d.text == date:
        d.click()
        break

# Add some wait time to observe the result
time.sleep(3)

# Close the browser
driver.quit()