import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging


class MainTestCase(unittest.TestCase):
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('grocery_test.log', mode='w', encoding='utf-8')
    logger.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

def setUp(self):
        self.driver = webdriver.Chrome("C:\webdrivers\chromedriver-win64\chromedriver.exe")
        self.addCleanup(self.driver.quit)



def test_grocery31(self):
      


def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)





       
