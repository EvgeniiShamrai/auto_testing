import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


url = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print('\n start browser for test')
    browser = webdriver.Chrome()
    yield browser
    print('\n quit browser')
    browser.quit()

class TestMainPage:
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self,browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR,'#login_link')

    @pytest.mark.regression
    @pytest.mark.win7
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR,'.basket-mini .btn-group > a')
