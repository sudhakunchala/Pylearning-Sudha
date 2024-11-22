from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj= Service("C:/Users/sudha/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

#CSS Selector combinations
# 1.tag & id combination  (tag is optional) syntax: tagname#value of id :input#email
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")  # tag name is option, without tagname we can use css selector


#2. tag & class combination syntax: tagname.valueof the class : input.inputtext _55r1 _6luy
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc")   # beacuse of class name is having some empty space , so it is giving error, so we should take the class name before the empty space
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc")  #tage name is optonal


#3. tag & attribute combination: tagename[attribute=value]
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc") # tage name is optional

#4. tag, class & attribute combination: if tag and class are name in the elements then we can go for tag, class and attribute combination
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("xyz")

input("Press Enter to close the browser...")
driver.quit()
