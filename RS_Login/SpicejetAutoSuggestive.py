import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


driver.get("https://www.spicejet.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input.css-1cwyjr8").send_keys('tir')
#driver.find_element(By.CSS_SELECTOR,"input.css-1cwyjr8[type='text']").send_keys("pun")

texts1 = driver.find_element(By.XPATH,"//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]")
texts = driver.find_elements(By.XPATH,'//*[@id="main-container"]/div/div[1]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]')
#print(texts1)
# print(type(texts))
# for text_new in texts:
#     print(text_new.text)
time.sleep(3)

options = driver.find_elements(By.XPATH,'//*[@id="main-container"]/div/div[1]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]')

options1 = driver.find_element(By.XPATH,"//div[contains(text(), 'Tirupati') and @class='css-76zvg2 r-cqee49 r-ubezar r-1kfrs79']")
print(options1.text)
counter = 0
print("options")
for option in options:
    counter += 1
    print(option.text)
    print(len(option.text))
    if option.text == "Pune":
        print("check3")
        option.click()










