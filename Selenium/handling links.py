from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj_ser)

driver.get("https://www.w3schools.com/")
driver.maximize_window()

#click on link
#driver.find_element(By.LINK_TEXT,"HTML Tutorial").click()

# find number of links
# you need find common attribute to all the links  i.e a
links=driver.find_elements(By.TAG_NAME,'a')
print('Number of links:',len(links))

# Name all the links in the console window
for link in links:
    print(link.text)

quit()
