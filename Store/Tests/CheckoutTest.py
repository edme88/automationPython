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
        assert product_page.checkTitle() in 'Viva Glam Lipstick'
        product_page.checkUnitPrice('$5.00') ##assert
        product_page.changeColor('Viva Glam II')
        product_page.changeQty('3')
        time.sleep(2)
        product_page.checkTotalPrice('$15.00') ##assert
        product_page.clickCart()

        ## Step 6: Checkout Shopping //Validar nombre del producto, color, precio unitario, cantidad, precio total y Titulo SHopping Cart
        assert 'SHOPPING CART' in shopping_page.checkTitle()
        assert 'Viva Glam Lipstick' in shopping_page.checkProductName()
        assert '- Color Viva Glam II' in shopping_page.checkProductColor()
        assert '$5.00' in shopping_page.checkProductUnitPrice()
        assert '3' in shopping_page.checkProductQuantity()
        assert '$15.00' in shopping_page.checkProductTotalPrice()
        shopping_page.clickCheckout()

        ## Step 7: Checkout Confirmation //Validar Shipping, Payment (Cash on delivery), y order sumary (cantidad, producto, color, subtotal, flat shipping y total)
        assert 'CHECKOUT CONFIRMATION' in checkout_page.getTitle()
        ## Shipping
        assert 'Shipping' in checkout_page.getShippingTitle()
        assert 'Agus Alici' in checkout_page.getShippingName()
        assert '358 4256985' in checkout_page.getShippingName()
        assert 'Jujuy 1214' in checkout_page.getShippingAddress()
        assert 'West Loop South' in checkout_page.getShippingAddress()
        assert 'Cordoba' in checkout_page.getShippingAddress()
        assert '5000' in checkout_page.getShippingAddress()
        assert 'Argentina' in checkout_page.getShippingAddress()
        assert 'Flat Shipping Rate' in checkout_page.getShippingCondition()
        ## Payment
        assert 'Payment' in checkout_page.getPaymentTitle()
        assert 'Agus Alici' in checkout_page.getPaymentName()
        assert '358 4256985' in checkout_page.getPaymentName()
        assert 'Jujuy 1214' in checkout_page.getPaymentAddress()
        assert 'West Loop South' in checkout_page.getPaymentAddress()
        assert 'Cordoba' in checkout_page.getPaymentAddress()
        assert '5000' in checkout_page.getPaymentAddress()
        assert 'Argentina' in checkout_page.getPaymentAddress()
        assert 'Cash On Delivery' in checkout_page.getPaymentCondition()
        ## Cart
        assert 'Items in your cart' in checkout_page.getCartTitle()
        assert 'Viva Glam Lipstick' in checkout_page.getProductTitle()
        assert '- Color Viva Glam II' in checkout_page.getProductColor()
        assert '$5.00' in checkout_page.getProductUnitPrice()
        assert '3' in checkout_page.getProductQuantity()
        assert '$15.00' in checkout_page.getProductTotalPrice()
        ## Order Summary
        assert 'ORDER SUMMARY' in checkout_page.getOrderSummaryTitle()
        assert 'Viva Glam Lipstick' in checkout_page.getOrderSummaryProduct()
        assert '- Color Viva Glam II' in checkout_page.getOrderSummaryColor()
        assert '$15.00' in checkout_page.getOrderSummarySuntotal()
        assert '$2.00' in checkout_page.getOrderSummaryShippingRate()
        assert '$17.00' in checkout_page.getOrderSummaryTotal()
        checkout_page.clickConfirmationBtn()

        ## Step 8: Confirmation Page
        time.sleep(10)
        assert 'YOUR ORDER HAS BEEN PROCESSED!' in confirmation_page.getTitle()

    """
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")"""

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/"), verbosity=2)