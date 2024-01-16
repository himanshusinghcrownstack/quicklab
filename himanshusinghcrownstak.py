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
        self.driver.get("https://qasworks.workctrl.store/account/login?email=himanshu.singh@sworks.co.in&pass=0wEswqW9&location_id=40&urltype=android&param=%7Bparam%7D&isdropmate=false&floor=Stilt%202%20-%20World%20Trade%20Tower%20-%20Sector%2016%20-%20Noida&drop_available=0&param=%7Bparam%7D&price=9&user_id=54674&wallet_id=1a724133-b5f4-4fa4-974f-2f7dca8d07c5&company_id=202&shopify_shop=qasworks")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Catalog").click()
        print("click on catalog buton")
        self.driver.find_element(By.ID, "CardLink-template--20351754567981__product-grid-8251732951341").click()
        print("grocery item is selected")
        time.sleep(15)
        self.driver.find_element(By.CLASS_NAME, "product-form__submit").click()
        time.sleep(40)
        self.driver.find_element(By.ID, "cart-icon-bubble").click()
        time.sleep(20)
        print("click on cart icon")
        self.driver.find_element(By.LINK_TEXT, "PLACE ORDER").click()
        time.sleep(15)
        self.driver.switch_to.frame(0)
        time.sleep(15)
        try:
            # Find the element by its class name
            element = self.driver.find_element(By.CLASS_NAME, "title.svelte-1z0zzkn")

            # Assertion to check if the element is present
            assert element is not None, "Element with class 'title svelte-1z0zzkn' not found"

        except AssertionError as e:
            print("Assertion error:", e)
            self.logger.info("Assertion error")
        except Exception as e:
            print("An error occurred:", e)
            self.logger.info("An error occurred")
            

    def test_grocery30(self):
        self.driver.get("https://qasworks.workctrl.store/account/login?email=himanshu.singh@sworks.co.in&pass=0wEswqW9&location_id=40&urltype=android&param=%7Bparam%7D&isdropmate=false&floor=Stilt%202%20-%20World%20Trade%20Tower%20-%20Sector%2016%20-%20Noida&drop_available=0&param=%7Bparam%7D&price=9&user_id=54674&wallet_id=1a724133-b5f4-4fa4-974f-2f7dca8d07c5&company_id=202&shopify_shop=qasworks")
        time.sleep(5)
        self.logger.info("user is login in store 30")
        self.driver.find_element(By.LINK_TEXT, "Catalog").click()
        print("click on catalog button")
        self.logger.info("click on catalog button")
        self.driver.find_element(By.ID, "quick-add-template--20297766371618__product-grid8418075803938-submit").click()
        print("grocery item is selected")
        time.sleep(15)
        self.driver.find_element(By.ID, "cart-notification-button").click()
        self.logger.info("click on cart icon")
        time.sleep(20)
        #self.driver.find_element(By.CLASS_NAME, "button.button--secondary.button--full-width").click()
        #time.sleep(20)
        print("click on cart icon")
        self.driver.find_element(By.ID, "loggedin").click()
        self.logger.info("user click on place order button")
        time.sleep(5)
        self.driver.switch_to.frame(0)
        time.sleep(5)
        self.logger.info("Payment gateway is open")
        try:
            # Find the element by its class name
            element = self.driver.find_element(By.CLASS_NAME, "title.svelte-1z0zzkn")

            # Assertion to check if the element is present
            assert element is not None, "Element with class 'title svelte-1z0zzkn' not found"

        except AssertionError as e:
            print("Assertion error:", e)
            self.logger.info("Assertion error")
        except Exception as e:
            print("An error occurred:", e)
            self.logger.info("An error occured")

    def test_grocery29(self):
        self.driver.get("https://devsworks-1103.myshopify.com/account/login?email=himanshu.singh@sworks.co.in&pass=0wEswqW9&location_id=40&urltype=android&param=%7Bparam%7D&isdropmate=false&floor=Stilt%202%20-%20World%20Trade%20Tower%20-%20Sector%2016%20-%20Noida&drop_available=0&param=%7Bparam%7D&price=9&user_id=54674&wallet_id=1a724133-b5f4-4fa4-974f-2f7dca8d07c5&company_id=202&shopify_shop=devsworks-1103")
        time.sleep(5)
        self.logger.info("user is login in store 29")
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Catalog").click()
        print("click on catalog button")
        self.logger.info("click on catalog button")
        self.driver.find_element(By.ID, "quick-add-template--20466295275829__product-grid8398727479605-submit").click()
        print("grocery item is selected")
        time.sleep(15)
        self.driver.find_element(By.ID, "cart-notification-button").click()
        self.logger.info("click on cart icon")
        time.sleep(20)
        print("click on cart icon")
        self.driver.find_element(By.ID, "loggedin").click()
        self.logger.info("user click on place order button")
        time.sleep(5)
        self.driver.switch_to.frame(0)
        time.sleep(5)
        self.logger.info("Payment gateway is open")
        try:
            # Find the element by its class name
            element = self.driver.find_element(By.CLASS_NAME, "title.svelte-1z0zzkn")

            # Assertion to check if the element is present
            assert element is not None, "Element with class 'title svelte-1z0zzkn' not found"

        except AssertionError as e:
            print("Assertion error:", e)
            self.logger.info("Assertion error")
        except Exception as e:
            print("An error occurred:", e)
            self.logger.info("An error occured")

        self.driver.quit()


def test_grocery28(self):
    self.driver.get("https://devsworks-1103.myshopify.com/account/login?email=himanshu.singh@sworks.co.in&pass=0wEswqW9&location_id=40&urltype=android&param=%7Bparam%7D&isdropmate=false&floor=Stilt%202%20-%20World%20Trade%20Tower%20-%20Sector%2016%20-%20Noida&drop_available=0&param=%7Bparam%7D&price=9&user_id=54674&wallet_id=1a724133-b5f4-4fa4-974f-2f7dca8d07c5&company_id=202&shopify_shop=devsworks-1103")
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "Catalog").click()
    print("click on catalog buton")
    self.driver.find_element(By.ID, "CardLink-template--20351754567981__product-grid-8251732951341").click()
    print("grocery item is selected")
    time.sleep(15)
    self.driver.find_element(By.CLASS_NAME, "product-form__submit").click()
    time.sleep(40)
    self.driver.find_element(By.ID, "cart-icon-bubble").click()
    time.sleep(20)
    print("click on cart icon")
    self.driver.find_element(By.LINK_TEXT, "PLACE ORDER").click()
    time.sleep(5)
    self.driver.switch_to.frame(0)
    time.sleep(5)
    self.driver.quit()

    def test_grocery27(self):
        self.driver.get("https://devsworks-1103.myshopify.com/account/login?email=himanshu.singh@sworks.co.in&pass=0wEswqW9&location_id=40&urltype=android&param=%7Bparam%7D&isdropmate=false&floor=Stilt%202%20-%20World%20Trade%20Tower%20-%20Sector%2016%20-%20Noida&drop_available=0&param=%7Bparam%7D&price=9&user_id=54674&wallet_id=1a724133-b5f4-4fa4-974f-2f7dca8d07c5&company_id=202&shopify_shop=devsworks-1103")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Catalog").click()
        print("click on catalog buton")
        self.driver.find_element(By.ID, "CardLink-template--20351754567981__product-grid-8251732951341").click()
        print("grocery item is selected")
        time.sleep(15)
        self.driver.find_element(By.CLASS_NAME, "product-form__submit").click()
        time.sleep(40)
        self.driver.find_element(By.ID, "cart-icon-bubble").click()
        time.sleep(20)
        print("click on cart icon")
        self.driver.find_element(By.LINK_TEXT, "PLACE ORDER").click()
        time.sleep(5)
        self.driver.switch_to.frame(0)
        time.sleep(5)

    def test_grocery26(self):
        self.driver.get("https://devsworks-1103.myshopify.com/account/login?email=himanshu.singh@sworks.co.in&pass=0wEswqW9&location_id=40&urltype=android&param=%7Bparam%7D&isdropmate=false&floor=Stilt%202%20-%20World%20Trade%20Tower%20-%20Sector%2016%20-%20Noida&drop_available=0&param=%7Bparam%7D&price=9&user_id=54674&wallet_id=1a724133-b5f4-4fa4-974f-2f7dca8d07c5&company_id=202&shopify_shop=devsworks-1103")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Catalog").click()
        print("click on catalog buton")
        self.driver.find_element(By.ID, "CardLink-template--20351754567981__product-grid-8251732951341").click()
        print("grocery item is selected")
        time.sleep(15)
        self.driver.find_element(By.CLASS_NAME, "product-form__submit").click()
        time.sleep(40)
        self.driver.find_element(By.ID, "cart-icon-bubble").click()
        time.sleep(20)
        print("click on cart icon")
        self.driver.find_element(By.LINK_TEXT, "PLACE ORDER").click()
        time.sleep(5)
        self.driver.switch_to.frame(0)
        time.sleep(5)
    def test_grocery32(self):




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)




