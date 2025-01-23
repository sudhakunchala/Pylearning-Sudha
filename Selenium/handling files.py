from selenium import webdriver

from selenium.webdriver.common.by import By
import time

def chrome_setup():# creating a function and keep the below code in the function
    from selenium.webdriver.chrome.service import Service
    # Setup Chrome WebDriver
    ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    return driver

driver=chrome_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(5)

driver.quit()
