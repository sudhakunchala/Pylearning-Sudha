from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# Setup Chrome WebDriver
ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1. Count no of rows and columns in a table

noofRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
noofColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))
print(noofRows) #7
print(noofColumns) #4

#2.Read specific row or column data
# Example we need to get the 5 row and 1 column data

data=driver.find_element(By.XPATH,"//table[@name= 'BookTable' ]/tbody/tr[5]/td[1]").text
#print(data)

#3.Read all the rows and colums data
# print("printing all the rows and columns data.....")
# for r in range(2,noofRows+1):
#     for c in range(1,noofColumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name= 'BookTable' ]/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         # the above one is syntax for dynamic Xpath
#         print(data,end='     ') # this will give data in tabular form
#     print()

#4. Reas the data based on the condition(List books name whose author is Mukesh)
for r in range(2,noofRows+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text # column 2 is constant
    if authorname=="Mukesh":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text # column 1 is bookname
        print(bookname,'       ',authorname)






driver.close()


