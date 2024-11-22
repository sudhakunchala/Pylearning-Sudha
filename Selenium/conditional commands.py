from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj_ser)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed and is_enabled
search_box=driver.find_element(By.XPATH,"//input[@id='small-searchterms']") # after finding the element, we can give some varaible name to store it and using that variable you can use is_displayed() method
print("Display Status:",search_box.is_displayed()) # if the search box is there, then it will return true
print("Display Status:",search_box.is_enabled()) # if the search box is enabled state, then it will return true


#is_selected(): for radia buttons and check boxes
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()

print("After clicking Male radio button:")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()

print("After clicking female radio button:")
print(rd_male.is_selected())
print(rd_female.is_selected())



input("Press enter to close the app...")
driver.quit()