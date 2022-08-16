# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     time.sleep(4)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")

import math
import time

import pytest
from selenium.webdriver.common.by import By

mass = ""

@pytest.mark.parametrize('num', [236895,236896,236897,236898,236899,236903,236904,236905])
def test_answer(browser, num):
    global mass
    browser.get(f'https://stepik.org/lesson/{num}/step/1')
    answer = math.log(int(time.time()))
    browser.implicitly_wait(10)
    time.sleep(4)
    browser.find_element(By.CSS_SELECTOR, ".quiz-component .ember-view").send_keys(str(answer))
    time.sleep(4)
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    time.sleep(3)
    text_out = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    try:
        assert text_out == "Correct!", "response text is not correct"
    except AssertionError:
        mass += text_out
        print(mass)


