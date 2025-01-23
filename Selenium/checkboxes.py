import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj_ser)

driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
driver.maximize_window()

# 1.How to select specific checkbox
#driver.find_element(By.XPATH,"(//input[@id='isAgeSelected'])[1]").click()

# 2.Selecting multiple checkboxes
# for this create Xpath with commonly having for all checkboxes
# Xpath: //input[@type='checkbox' and contains(@id,'ex1')]

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'ex1')]")
print(len(checkboxes)) # this is give the count of checkboxes i.e 4

# #Approch1 : to select all checkboxes using for loop
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#Approach2:
# for checkbox in checkboxes:
#     checkbox.click()

#3.Selecting checkboxes by your choice

# for checkbox in checkboxes:
#     options=checkbox.get_attribute('id')
#     if options=='ex1-check1' or options=='ex1-check4':
#         checkbox.click()

#4.Selecting checkboxes from bottom (if you want to select bottom 2 checkboxes)
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#5.Selecting checkboxes from upper(if you want to select upper 2 checkboxes)
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

time.sleep(5)
 #6.clearing all checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()





input("press enter to close the app..")
driver.quit()