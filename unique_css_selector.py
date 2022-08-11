import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class UniqueSelector(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.urls = ["http://suninjuly.github.io/registration1.html","http://suninjuly.github.io/registration2.html"]

    def test_find_unique_selector_by_first_url(self):
        self.driver.get(self.urls[0])
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Jonh")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Travolta")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("www@mail.ru")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        final_text = self.driver.find_element(By.TAG_NAME, "h1").text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(expected_text, final_text, "The text does not match the expected result")

    def test_find_unique_selector_by_second_url(self):
        self.driver.get(self.urls[1])
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Jonh")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Travolta")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("www@mail.ru")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        final_text = self.driver.find_element(By.TAG_NAME, "h1").text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(expected_text, final_text, "The text does not match the expected result")

if __name__ == '__main__':
    unittest.main()