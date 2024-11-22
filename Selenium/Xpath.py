from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

obj_ser=Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj_ser)

driver.get("https://www.amazon.com/")
driver.maximize_window()

#absolute path:
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/div/input").send_keys("Toys") # Search button
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()


#relative path:
# driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("Toys")
# driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()

# contains() and starts-with()
driver.find_element(By.XPATH,"//input[contains(@id,'two')]").send_keys("Toys")
driver.find_element(By.XPATH,"//input[starts-with(@id,'nav')]").click()


input("press enter to close the website...")
driver.quit()