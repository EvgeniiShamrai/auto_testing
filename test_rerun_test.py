import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"

def test_first_test(browser):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, '#login_link')


def test_second_test(browser):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR,"#magic_link")
