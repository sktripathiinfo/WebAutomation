import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


driver.get("https://www.spicejet.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input.css-1cwyjr8").send_keys('Pun')

time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,"input.css-1cwyjr8").get_attribute("value"))

cities = driver.find_elements(By.CSS_SELECTOR,"div[class='css-1dbjc4n r-knv0ih r-1k1q3bj r-ql8eny r-1dqxon3'] div")

print(len(cities))

for city in cities:
    if city.text == "Pune":
        city.click()
        break

print(driver.find_element(By.CSS_SELECTOR,"input.css-1cwyjr8").get_attribute("value"))


driver.find_element(By.CSS_SELECTOR,"input.css-1cwyjr8").send_keys('tir')
time.sleep(5)

print(driver.find_element(By.CSS_SELECTOR,"input.css-1cwyjr8").get_attribute("value"))

cities2 = driver.find_elements(By.CSS_SELECTOR,"div[class='css-1dbjc4n r-knv0ih r-1k1q3bj r-ql8eny r-1dqxon3'] div")

print(len(cities2))

for city in cities2:
    if city.text == "Tirupati":
        city.click()
        break

print(driver.find_element(By.CSS_SELECTOR,"input.css-1cwyjr8").get_attribute("value"))
