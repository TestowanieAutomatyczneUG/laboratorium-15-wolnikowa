import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        driver.get("https://duckduckgo.com/")
        # driver.find_element()
        # time.sleep(5)
        driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        time.sleep(5)
        driver.find_element_by_id("search_button_homepage").submit()
        time.sleep(5)
        self.assertEqual(driver.title, "Selenium at DuckDuckGo")
        driver.quit()


if __name__ == '__main__':
    unittest.main()