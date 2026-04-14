from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin

url = 'https://suninjuly.github.io/math.html'

with webdriver.Chrome() as driver:
    driver.implicitly_wait(5)
    driver.get(url)

    input_value = driver.find_element(By.ID, 'input_value')
    x = int(input_value.text)
    capcha_value = log(abs(12 * sin(x)))

    field = driver.find_element(By.ID, 'answer')
    field.send_keys(capcha_value)

    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = driver.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    button = driver.find_element(By.CLASS_NAME, 'btn')
    button.click()

    alert = driver.switch_to.alert
    code = alert.text.split(': ')[-1]
    print(code)
