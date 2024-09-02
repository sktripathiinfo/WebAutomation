import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/angularpractice/")

print (driver.title)
# maximizing the windows
driver.maximize_window()



driver.find_element(By.NAME,"name").send_keys("shubham tripathi")
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234567")
driver.find_element(By.ID,"exampleCheck1").click()

# Static Dropdown Concept

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")



driver.find_element(By.XPATH,"//input[@value='Submit']").click()








time.sleep(5)
driver.close()