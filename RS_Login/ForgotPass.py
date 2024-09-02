import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/auth/login")
print(driver.title)


driver.find_element(By.ID,"userEmail").send_keys("sktripathiinfo@gmail.com")
# driver.find_element(By.ID,"userPassword").send_keys("sktripathi")
#will work on it later

time.sleep(5)