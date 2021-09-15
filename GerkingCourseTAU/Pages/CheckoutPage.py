from selenium.webdriver.common.by import By


class CheckoutPageLocators():
    CONFIRM_ORDER_BTN = (By.ID, 'checkout_btn')

class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

    def getBtnConfirmOrder(self):
        return self.driver.find_element(*CheckoutPageLocators.CONFIRM_ORDER_BTN)
