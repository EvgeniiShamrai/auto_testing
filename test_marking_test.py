import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture()
def browser():
    print("\n Start browser for test ..")
    browser = webdriver.Chrome()
    yield browser
    print("\n Browser quit ..")
    browser.quit()

class TestMainPage:
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self,browser):
        browser.get(url)
        browser.find_element(By.ID,"login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_main_page(self,browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

