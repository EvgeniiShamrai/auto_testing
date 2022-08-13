from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\n start browser for test suit 1...")
        self.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suit 1...")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        print("start test link 1")
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_link_on_the_main_page(self):
        print("start test basket 1")
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("\n start browser for test suit 2...")
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test suit 2...")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        print("start test link 2")
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_link_on_the_main_page(self):
        print("start test basket 2")
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

