from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

url = 'https://suninjuly.github.io/redirect_accept.html'

with webdriver.Chrome() as driver:
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    new_window = driver.window_handles[-1]
    driver.switch_to.window(new_window)

    input_value = driver.find_element(By.ID, 'input_value')
    x = int(input_value.text)
    capcha_value = log(abs(12 * sin(x)))

    field = driver.find_element(By.ID, 'answer')
    field.send_keys(capcha_value)

    button = driver.find_element(By.CLASS_NAME, 'btn')
    button.click()

    alert = driver.switch_to.alert
    code = alert.text.split(': ')[-1]
    print(code)
