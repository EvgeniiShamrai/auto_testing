import math
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driwer = webdriver.Chrome()

try:
    url = "https://suninjuly.github.io/math.html"
    driwer.get(url)
    sleep(1)
    x_value = driwer.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_value)
    driwer.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    sleep(1)
    driwer.find_element(By.CSS_SELECTOR, "[required].form-check-input").click()
    sleep(1)
    # driwer.find_element(By.CSS_SELECTOR, "input[value = robots]").click()
    check_radio = driwer.find_element(By.ID,"peopleRule").get_attribute("checked")
    sleep(1)
    assert check_radio is not None
    
    driwer.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    sleep(6)
    driwer.quit()
