import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH,"//div[@class='products']/ div")

count = len(results)
print(count)



assert count > 0

# chaining web element

for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='cart-preview active'] button[type='button']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait = WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"promoInfo")))


print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
