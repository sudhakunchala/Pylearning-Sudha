from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/self::a").text
# print(text_msg)

#parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/parent::td").text
# print(text_msg)

#ancestor
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels Co')]/ancestor::tr").text
print(text_msg)



input("press enter to close the site...")
driver.quit()