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
driver.implicitly_wait(5)


driver.get("https://only-testing-blog.blogspot.com/2014/09/selectable.html")
driver.maximize_window()

button=driver.find_element(By.XPATH,"//ol[@id='selectable']//li[3]")

act=ActionChains(driver)
act.context_click(button).click().perform()
time.sleep(5)
driver.quit()
