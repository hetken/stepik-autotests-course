from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

url = 'http://suninjuly.github.io/registration2.html'

# Test data
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)

first_name_field = driver.find_element(By.CSS_SELECTOR, '.first_block .first')
first_name_field.send_keys(first_name)
email_field = driver.find_element(By.CSS_SELECTOR, '.first_block .third')
email_field.send_keys(email)

button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
button.click()
time.sleep(1)

welcome_element = driver.find_element(By.TAG_NAME, 'h1')
welcome_text = welcome_element.text
assert welcome_text == 'Congratulations! You have successfully registered!'

driver.quit()
