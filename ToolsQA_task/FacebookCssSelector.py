import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/login/")
print(driver.title)
print (driver.current_url)
driver.maximize_window()

# here if we do not write tag name ,the code will work
# tag & id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("shubham")

# tag & class

# driver.find_element(By.CSS_SELECTOR,"input.inputtext._55r1.inputtext._9npi.inputtext._9npi ").send_keys("123456789")

# tag &attribute  ---syntax -- tagname[atribute='value']
# driver.find_element(By.CSS_SELECTOR,"input[placeholder=Email address or phone number]").send_keys("12345")

# without tagname
# [placeholder="Email address or phone number"]
# driver.find_element(By.CSS_SELECTOR,"[autocomplete='username']").send_keys("1234567")


# X-path

# Absolute x-path

driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input").send_keys("shubham tripathi")


driver.find_element(By.CSS_SELECTOR,"div[class='_55r1 _1kbt']").send_keys("11111123")



# relative xpath







time.sleep(5)