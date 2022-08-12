import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception_1():
    try:
        driver = webdriver.Chrome()
        driver.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Кнопки 'Отправить' на странице не должно быть")
    finally:
        driver.quit()


def test_exception_2():
    try:
        driver = webdriver.Chrome()
        driver.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CSS_SELECTOR, "exp.button.btn")
            pytest.fail("Кнопки 'Отправить' на странице не должно быть")
    finally:
        driver.quit()
