# These are the actions we need to automate
#ctl+A
#ctl+c
#Tab
#Clr+V

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

# Type data into input1 box
input1.send_keys("This is Sudha")

# Input1-->Ctrl+A keyboard action
act=ActionChains(driver)

# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

#Single statement
act.key_down(Keys.CONTROL).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#Input1-->Ctl+C--->copy the text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Press Tab key to navigate ti Input2
act.send_keys(Keys.TAB).perform()

# Input2-->ctrl V--->paste the text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)
driver.quit()