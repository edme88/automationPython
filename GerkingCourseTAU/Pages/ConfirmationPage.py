from selenium.webdriver.common.by import By


class ConfirmationPageLocators():
    PARAGRAF_ORDER = (By.CSS_SELECTOR, 'h4+p+p')

class ConfirmationPage():

    def __init__(self, driver):
        self.driver = driver

    def getOrderText(self):
        return self.driver.find_element(*ConfirmationPageLocators.PARAGRAF_ORDER)
