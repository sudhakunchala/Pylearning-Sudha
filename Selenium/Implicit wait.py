
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

obj_ser=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj_ser)
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,'q')

searchbox.send_keys("Selenium")
searchbox.submit()


driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

input("press enter to close the app..")
driver.quit()
