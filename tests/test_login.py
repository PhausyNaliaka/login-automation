from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

login_page = "file:///C:/Users/phaustine.mulongo/Desktop/Login-test-project/website/index.html"

# -------- Test 1: Valid Login --------
print("Running Test: Valid Login")

driver.get(login_page)

time.sleep(2)

email = driver.find_element(By.ID, "email")
email.send_keys("test@test.com")

password = driver.find_element(By.ID, "password")
password.send_keys("123456")

password.send_keys(Keys.RETURN)

time.sleep(3)

# -------- Test 2: Invalid Password --------
print("Running Test: Invalid Password")

driver.get(login_page)

time.sleep(2)

email = driver.find_element(By.ID, "email")
email.send_keys("test@test.com")

password = driver.find_element(By.ID, "password")
password.send_keys("wrong123")

password.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()

print("All tests completed")