from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

import time
from Store.Pages.IndexPage import IndexPage
from Store.Pages.LoginOrRegister import LoginOrRegisterPage
from Store.Pages.MenuPage import MenuPage
from Store.Pages.MakeUpPage import MakeUpPage
from Store.Pages.ProductPage import ProductPage
from Store.Pages.ShoppingCartPage import ShoppingCartPage
from Store.Pages.CheckoutConfirmation import CheckoutConfirmationPage
from Store.Pages.ConfirmationPage import ConfirmationPage
import HtmlTestRunner

class loginTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("../../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://automationteststore.com/")
        cls.driver.maximize_window()

    def test_login(self):
        index_page = IndexPage(self.driver)
        login_page = LoginOrRegisterPage(self.driver)
        menu_page = MenuPage(self.driver)
        makeUp_page = MakeUpPage(self.driver)
        product_page = ProductPage(self.driver)
        shopping_page = ShoppingCartPage(self.driver)
        checkout_page = CheckoutConfirmationPage(self.driver)
        confirmation_page = ConfirmationPage(self.driver)

        ## Step 1: Click Button Login or Register
        index_page.goToLoginOrRegisterPage()
        time.sleep(2)

        ## Step 2: Complete user and pass
        login_page.login('agusDarwoft', 'automation')

        ## Step 3: Click MakeUp Menu
        menu_page.clickMenuMakeUp()

        ## Step4: Select Lipstick
        makeUp_page.getVivaGlamLipStick()

        ## Step5: Change Quantity
        product_page.changeColor('Viva Glam II')
        product_page.changeQty('3')
        product_page.clickCart()

        ## Step 6: Checkout Shopping
        shopping_page.clickCheckout()

        ## Step 7: Checkout Confirmation
        assert 'CHECKOUT CONFIRMATION' in checkout_page.getTitle()
        checkout_page.clickConfirmationBtn()

        ## Step 8: Confirmation Page
        time.sleep(10)
        assert 'YOUR ORDER HAS BEEN PROCESSED!' in confirmation_page.getTitle()

    """@classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")"""

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/"), verbosity=2)