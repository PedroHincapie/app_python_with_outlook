import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.binary_location = '/usr/bin/google-chrome'

        cls.driver = webdriver.Chrome(options=chrome_options)
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get("http://www.platzi.com")

    def test_visit_wikipedia(self):
        self.driver.get("https://www.wikipedia.org")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(output="reportes", report_name="hello-world-report"),
    )
