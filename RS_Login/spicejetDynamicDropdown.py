import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the SpiceJet website and maximize the browser window
driver.get("https://www.spicejet.com/")
driver.maximize_window()

# Define selectors for reuse
input_selector = "input.css-1cwyjr8"
city_selector = "div[class='css-1dbjc4n r-knv0ih r-1k1q3bj r-ql8eny r-1dqxon3'] div"

# Wait for the input field to be visible and enter text 'Pun'
input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, input_selector)))
input_field.send_keys('Pun')

# Wait for the list of cities to be populated
cities = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, city_selector)))
print(len(cities))

# Click on the city 'Pune'
for city in cities:
    if city.text == "Pune":
        city.click()
        break

# Print the value of the input field after selection
print(input_field.get_attribute("value"))

# Clear the input field and enter new text 'tir'
input_field.clear()
input_field.send_keys('tir')

# Wait for the new list of cities to be populated
cities2 = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, city_selector)))
print(len(cities2))

# Click on the city 'Tirupati'
for city in cities2:
    if city.text == "Tirupati":
        city.click()
        break

# Print the value of the input field after the second selection
print(input_field.get_attribute("value"))

# Close the browser
driver.quit()
