# we need to install requests package from file-->python interpreter-->requests
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj_ser)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in all_links:
    url=link.get_attribute('href')
    try:
       res=requests.head(url)
    except:
         None
    if res.status_code>=400:
        print(url,"The link is broken")
        count+=1
    else:
        print(url,"valid link")

print("Total number of links:",count)

driver.quit()
