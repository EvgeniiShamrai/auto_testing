import time

from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"


def test_first(browser):
    browser.get(url)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
