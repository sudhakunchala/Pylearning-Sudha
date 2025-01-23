from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#capture cookies
cookies=driver.get_cookies()
print(len(cookies))
time.sleep(5)

#Print details of cookies
# for c in cookies:
#     print(c)

# #adding new cookie to the browser:
driver.add_cookie({"name":"Mycookie","value":"123456"})
cookies=driver.get_cookies()
print("After adding new cookie:",len(cookies))

# delete specific cookie from the browser
driver.delete_cookie("Mycookie")
cookies=driver.get_cookies()
print("After deleting new cookie:",len(cookies))

#delete all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("After deleting all cookies:",len(cookies))
driver.quit()