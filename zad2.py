import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_first(self):  # by_id
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-0").click()
        time.sleep(5)
        self.assertEqual(self.driver.title, "Selenium")
        self.driver.close()

    def test_third(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-2").click() #3wynik
        time.sleep(5)
        self.assertEqual(self.driver.title, "Selenium - Health Professional Fact Sheet")
        self.driver.close()

    def test_tagname(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-0").click()
        e = self.driver.find_elements(By.TAG_NAME, "section")
        time.sleep(5)
        self.assertEqual(len(e), 2)
        self.driver.close()

    def test_namer(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-0").click()
        val = self.driver.find_element(By.NAME, "generator").get_attribute("content")
        time.sleep(5)
        self.assertEqual(val, "Hugo 0.83.1")
        self.driver.close()

    def test_classname(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-0").click()
        self.driver.find_element(By.CLASS_NAME, "selenium-button").click()
        time.sleep(5)
        self.assertEqual(self.driver.title, "WebDriver | Selenium")
        self.driver.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()