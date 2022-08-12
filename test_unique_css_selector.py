import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class UniqueSelector(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()



    def test_find_unique_selector_by_first_url(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Jonh")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Travolta")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("www@mail.ru")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        sleep(1)
        final_text = self.driver.find_element(By.TAG_NAME, "h1").text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(expected_text, final_text, "The text does not match the expected result")
        self.driver.quit()

    def test_find_unique_selector_by_second_url(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Jonh")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Travolta")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("www@mail.ru")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        sleep(1)
        final_text = self.driver.find_element(By.TAG_NAME, "h1").text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(expected_text, final_text, "The text does not match the expected result")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()