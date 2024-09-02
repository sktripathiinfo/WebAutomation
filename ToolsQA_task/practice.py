import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()

#
# driver.find_element(By.CLASS_NAME,"").send_keys("facebook.com")

# by css selector
# driver.find_element(By.CSS_SELECTOR,"textarea[name='q']").send_keys("java")


# finding element by Id
# driver.find_element(By.ID,"APjFqb").send_keys("selenium")


# finding element by Class name
# driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("python")






time.sleep(5)