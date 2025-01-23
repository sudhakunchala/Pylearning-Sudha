from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

# Find the slider elements (min and max sliders)
min_slider = driver.find_element(By.XPATH, "//div[@class='price-range-block']//span[1]")
max_slider = driver.find_element(By.XPATH, "//div[@class='price-range-block']//span[2]")

# Print the initial location of the sliders
print("Location of sliders before moving...")
print(f"Min Slider location: {min_slider.location}")
print(f"Max Slider location: {max_slider.location}")

# Create an ActionChains object to perform drag and drop actions
act = ActionChains(driver)

# Perform drag and drop by offset on the sliders
act.drag_and_drop_by_offset(min_slider, 120, 0).perform()
act.drag_and_drop_by_offset(max_slider, 400, 0).perform()

# Wait to let the sliders move
time.sleep(2)  # Shorter wait to observe changes

# Print the location of the sliders after moving
print("Location of sliders after moving...")
print(f"Min Slider location: {min_slider.location}")
print(f"Max Slider location: {max_slider.location}")

# Close the browser
driver.quit()