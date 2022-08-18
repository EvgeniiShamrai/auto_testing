import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_find_button_add_to_basket(browser):
    browser.get(url)
    time.sleep(30)
    button_add_basket= browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed()
    assert button_add_basket, "The Button 'add to basket' is not on the page"

