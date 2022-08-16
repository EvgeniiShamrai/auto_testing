
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85 import browser


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')


# Фикстура для определения веб драйвра и после отработки тестов драйвер закрывается
@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == 'chrome':
        print('\n start browser Chrome..')
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
        print('\n start browser Firefox..')
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\n quit browser..')
    browser.quit()

