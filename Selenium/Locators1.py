# How to launch browser and open the browser:
from selenium import webdriver    # need to import webdriver
from selenium.webdriver.chrome.service import Service  # this is required for launching browser
from selenium.webdriver.common.by import By

ser_obj=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://www.amazon.com/")  # to open the browser
driver.maximize_window()   # to maximize the window

#driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Laptop")  # finding element using id locator
#driver.find_element(By.LINK_TEXT,"Holiday Deals").click()      # finding element using link text
#driver.find_element(By.PARTIAL_LINK_TEXT,"Holi").click()   # finding element using partial link text

sliders=driver.find_elements(By.CLASS_NAME,"a-carousel-card") # we can find multiple elements using class name locator
print(len(sliders))

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))


input("Press Enter to close the browser...")
driver.quit()



