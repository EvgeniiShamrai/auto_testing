import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def driver():
    print("\n start browser for test..")
    driver = webdriver.Chrome()
    return driver

class TestMainPage1:
    def test_guest_should_see_login_link(self, driver):
        driver.get(url)
        driver.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        driver.get(url)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")