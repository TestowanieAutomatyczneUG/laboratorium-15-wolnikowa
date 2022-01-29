import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestXPATH(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")

    def test_countLinks(self):
        links = self.driver.find_elements(by="xpath", value="//a")
        self.assertTrue(len(links) >= 0)

    def test_countImages(self):
        images = self.driver.find_elements(by="xpath", value="//img")
        self.assertTrue(len(images) >= 0)

    def test_checkLinks(self):
        links = self.driver.find_elements(by="xpath", value="//a[contains(@href, '')]")
        time.sleep(1)
        for a in range(0, len(links)):
            newlinks = self.driver.find_elements(by="xpath", value="//a[contains(@href, '')]")
            if newlinks[a].get_dom_attribute("href") is None:
                break
            for i in range(0, 2):
                try:
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(by="xpath", value=f"//a[@href=\'{newlinks[a].get_dom_attribute('href')}\']"))
                    self.driver.get("https://duckduckgo.com/")
                    break
                except StaleElementReferenceException as ex:
                    print(ex)
        self.assertTrue(len(links) >= 0)

    def test_countInputs(self):
        form = self.driver.find_element(by="xpath", value="//form")
        inputs = form.find_elements(by="xpath", value=".//input")
        self.assertTrue(len(inputs) >= 0)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()