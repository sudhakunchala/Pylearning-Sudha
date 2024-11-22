from selenium import webdriver
from selenium.webdriver.chrome.service import Service

obj_ser=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj_ser)

driver.get("https://www.amazon.com/")
driver.maximize_window()

print(driver.title)  # gives the title of the current web page
print(driver.current_url) #gives current url of the application
print(driver.page_source) # returns source code of the page

input("press enter to close the app...")
driver.quit()