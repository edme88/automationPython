import unittest
from selenium.webdriver.common.by import By

class CheckoutConfirmationPage(unittest.TestCase):
    TITLE = (By.CSS_SELECTOR, 'h1')
    BTN_CONFIRM_ORDER = (By.ID, 'checkout_btn')
    SHIPPING_TITLE = (By.CSS_SELECTOR, 'h4.heading4:nth-of-type(1)')
    SHIPPING_NAME = (By.CSS_SELECTOR, '.confirm_shippment_options td.align_left:nth-of-type(1)')
    SHIPPING_ADDRESS = (By.CSS_SELECTOR, '.confirm_shippment_options td.align_left:nth-of-type(2)')
    SHIPPING_CONDITION = (By.CSS_SELECTOR, '.confirm_shippment_options td.align_left:nth-of-type(3)')
    PAYMENT_TITLE = (By.CSS_SELECTOR, 'h4.heading4:nth-of-type(2)')
    PAYMENT_NAME = (By.CSS_SELECTOR, '.confirm_payment_options td.align_left:nth-of-type(1)')
    PAYMENT_ADDRESS = (By.CSS_SELECTOR, '.confirm_payment_options td.align_left:nth-of-type(2)')
    PAYMENT_CONDITION = (By.CSS_SELECTOR, '.confirm_payment_options td.align_left:nth-of-type(3)')
    CART_TITLE = (By.CSS_SELECTOR, 'h4.heading4:nth-of-type(3)')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'table.confirm_products td:nth-of-type(2) a')
    PRODUCT_COLOR = (By.CSS_SELECTOR, 'table.confirm_products small')
    PRODUCT_UNIT_PRICE = (By.CSS_SELECTOR, 'table.confirm_products td:nth-of-type(3)')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, 'table.confirm_products td:nth-of-type(4)')
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, 'table.confirm_products td:nth-of-type(5)')
    TABLE_SUBTOTAL = (By.CSS_SELECTOR, '.cart-info tr:nth-of-type(1)>td+td')
    TABLE_SHIPPING_RATE = (By.CSS_SELECTOR, '.cart-info tr:nth-of-type(2)>td+td')
    TABLE_TOTAL = (By.CSS_SELECTOR, '.cart-info tr:nth-of-type(2)>td+td')
    ORDER_SUMMARY_TITLE = (By.CSS_SELECTOR, 'h2.heading2')
    ORDER_PRODUCT = (By.CSS_SELECTOR, 'h2+table tr>td a')
    ORDER_COLOR = (By.CSS_SELECTOR, 'h2+table tr>td div')
    ORDER_UNIT_PRICE = (By.CSS_SELECTOR, 'h2+table tr>td+td')
    ORDER_SUBTITLE = (By.CSS_SELECTOR, 'div.gray_separator+table tr:nth-of-type(1)>td+td')
    ORDER_SHIPPING_RATE = (By.CSS_SELECTOR, 'div.gray_separator+table tr:nth-of-type(2)>td+td')
    ORDER_TOTAL = (By.CSS_SELECTOR, 'div.gray_separator+table tr:nth-of-type(3)>td+td')

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*self.TITLE).text

    def clickConfirmationBtn(self):
        self.driver.find_element(*self.BTN_CONFIRM_ORDER).click()

    def getShippingTitle(self):
        return self.driver.find_element(*self.SHIPPING_TITLE).text

    def getShippingName(self):
        return self.driver.find_element(*self.SHIPPING_NAME).text

    def getShippingAddress(self):
        return self.driver.find_element(*self.SHIPPING_ADDRESS).text

    def getShippingCondition(self):
        return self.driver.find_element(*self.SHIPPING_CONDITION).text

    def getPaymentTitle(self):
        return self.driver.find_element(*self.PAYMENT_TITLE).text

    def getPaymentName(self):
        return self.driver.find_element(*self.PAYMENT_NAME).text

    def getPaymentAddress(self):
        return self.driver.find_element(*self.PAYMENT_ADDRESS).text

    def getPaymentCondition(self):
        return self.driver.find_element(*self.PAYMENT_CONDITION).text

    def getCartTitle(self):
        return self.driver.find_element(*self.CART_TITLE).text

    def getProductTitle(self):
        return self.driver.find_element(*self.PRODUCT_TITLE).text

    def getProductColor(self):
        return self.driver.find_element(*self.PRODUCT_COLOR).text

    def getProductUnitPrice(self):
        return self.driver.find_element(*self.PRODUCT_UNIT_PRICE).text

    def getProductQuantity(self):
        return self.driver.find_element(*self.PRODUCT_QUANTITY).text

    def getProductTotalPrice(self):
        return self.driver.find_element(*self.PRODUCT_TOTAL_PRICE).text

    def getTableSubtotal(self):
        return self.driver.find_element(*self.TABLE_SUBTOTAL).text

    def getTableShippingRate(self):
        return self.driver.find_element(*self.TABLE_SHIPPING_RATE).text

    def getTableTotal(self):
        return self.driver.find_element(*self.TABLE_TOTAL).text

    def getOrderSummaryTitle(self):
        return self.driver.find_element(*self.ORDER_SUMMARY_TITLE).text

    def getOrderSummaryProduct(self):
        return self.driver.find_element(*self.ORDER_PRODUCT).text

    def getOrderSummaryColor(self):
        return self.driver.find_element(*self.ORDER_COLOR).text

    def getOrderUnitPrice(self):
        return self.driver.find_element(*self.ORDER_UNIT_PRICE).text

    def getOrderSummarySuntotal(self):
        return self.driver.find_element(*self.ORDER_SUBTITLE).text

    def getOrderSummaryShippingRate(self):
        return self.driver.find_element(*self.ORDER_SHIPPING_RATE).text

    def getOrderSummaryTotal(self):
        return self.driver.find_element(*self.ORDER_TOTAL).text