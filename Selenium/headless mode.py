from selenium import webdriver
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    ser_obj = Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver = webdriver.Chrome(service=ser_obj,options=ops)
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.quit()
