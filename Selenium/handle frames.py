import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()

# To handle frames we have swith_to.frame() command
# to use this command , we have multiple options
# swith_to.frame(name of the frame)
#swith_to.frame(id of the frame)
#switch_to.frame(webelement)

# Parent frame-top frame
driver.switch_to.frame("frame-top")

# Switch to left frame
driver.switch_to.frame("frame-left")
left_text=driver.find_element(By.TAG_NAME,"body").text
print("Left Frame text:",left_text)

# switching to parent
driver.switch_to.parent_frame()

#Swith to middle frame
driver.switch_to.frame("frame-middle")
middle_text=driver.find_element(By.ID,"content").text
print("middle frame text:",middle_text)

# switching to parent
driver.switch_to.parent_frame()

#Swith to right frame
driver.switch_to.frame("frame-right")
right_text=driver.find_element(By.TAG_NAME,"body").text
print("right frame text:",right_text)

# Switch back to the default content before accessing another top-level frame
# frame-bottom and frame-top are sibling frames, not parent-child. To switch to frame-bottom, you must first exit all frames by using driver.switch_to.default_content().
driver.switch_to.default_content()

#Swith to bottom frame
driver.switch_to.frame("frame-bottom")
bottom_text=driver.find_element(By.TAG_NAME,"body").text
print("bottom frame text:",bottom_text)



driver.quit()


