import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.ID,"firstName").send_keys("shubham")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("tripathi")
driver.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#userNumber").send_keys("1234567890")

# driver.find_element(By.XPATH,"//*[@id='subjectsContainer']/div/div[1]").send_keys("abc")

driver.find_element(By.XPATH,"(//div[@class='col-md-9 col-sm-12'])[6]").click()
time.sleep(5)

