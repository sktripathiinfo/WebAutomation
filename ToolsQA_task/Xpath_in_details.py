from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (assumes you have installed the ChromeDriver)
driver = webdriver.Chrome()

# Open the website
driver.get("https://money.rediff.com/gainers")

# Example 1: Absolute XPath
company_absolute_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/table/tbody/tr[3]/td[1]/a")
print("Absolute XPath: ", company_absolute_xpath.text)

# Example 2: Relative XPath
company_relative_xpath = driver.find_element(By.XPATH, "//a[contains(text(), 'Infosys')]")
print("Relative XPath: ", company_relative_xpath.text)

# Example 3: Ancestor Axis
ancestor_example = driver.find_element(By.XPATH, "//a[contains(text(), 'Infosys')]/ancestor::tr")
print("Ancestor Axis: ", ancestor_example.text)

# Example 4: Parent Axis
parent_example = driver.find_element(By.XPATH, "//a[contains(text(), 'Infosys')]/parent::td")
print("Parent Axis: ", parent_example.text)

# Example 5: Self Axis
self_example = driver.find_element(By.XPATH, "//a[contains(text(), 'Infosys')]/self::a")
print("Self Axis: ", self_example.text)

# Example 6: Child Axis
child_example = driver.find_element(By.XPATH, "//tr[3]/child::td[1]")
print("Child Axis: ", child_example.text)

# Example 7: Descendant Axis
descendant_example = driver.find_element(By.XPATH, "//table/descendant::a[contains(text(), 'Infosys')]")
print("Descendant Axis: ", descendant_example.text)

# Example 8: Following Axis
following_example = driver.find_element(By.XPATH, "//a[contains(text(), 'Infosys')]/following::tr[1]")
print("Following Axis: ", following_example.text)

# Example 9: Following-Sibling Axis
following_sibling_example = driver.find_element(By.XPATH, "//a[contains(text(), 'Infosys')]/following-sibling::td[1]")
print("Following-Sibling Axis: ", following_sibling_example.text)

# Example 10: Preceding Axis
preceding_example = driver.find_element(By.XPATH, "//a[contains(text(), 'Infosys')]/preceding::tr[1]")
print("Preceding Axis: ", preceding_example.text)

# Example 11: Preceding-Sibling Axis
preceding_sibling_example = driver.find_element(By.XPATH, "//a[contains(text(), 'Infosys')]/preceding-sibling::td[1]")
print("Preceding-Sibling Axis: ", preceding_sibling_example.text)

# Close the browser window
driver.quit()
