import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        chrome_options = Options()
        chrome_options.binary_location = '/usr/bin/google-chrome'

        self.driver = webdriver.Chrome(options=chrome_options)
        driver = self.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get("http://www.platzi.com")

    def test_visit_wikipedia(self):
        self.driver.get("https://www.wikipedia.org")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(output="reportes", report_name="hello-world-report"),
    )
