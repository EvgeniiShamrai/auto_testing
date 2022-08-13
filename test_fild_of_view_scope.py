import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def browser():
    print("\n start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\n quit browser..")
    browser.quit()

class TestMainPage1:

    def test_guest_should_see_login_link(self, browser: webdriver.Chrome):
        print("start test 1")
        browser.get(url)
        time.sleep(1)
        browser.find_element(By.ID, "login_link")
        print("finish test 1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser: webdriver.Chrome):
        print("start test 2")
        browser.get(url)
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test 2")