import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HeaderPageLocators():
    SEARCH_INPUT = (By.ID, 'filter_keyword')
    SEARCH_BTN = (By.CLASS_NAME, 'fa-search')
    PRODUCT_TITLE = (By.CLASS_NAME, 'bgnone')
    CHECKOUT_BTN = (By.CSS_SELECTOR, 'ul#main_menu_top li[data-id="menu_checkout"]')
    WELCOMEBACK_BTN = (By.CLASS_NAME, 'menu_text')

class HeaderPage():

    def __init__(self, driver):
        self.driver = driver

    def getSearchInput(self):
        return self.driver.find_element(*HeaderPageLocators.SEARCH_INPUT)

    def getSearchButton(self):
        return self.driver.find_element(*HeaderPageLocators.SEARCH_BTN)

    def getProductTitle(self):
        return self.driver.find_element(*HeaderPageLocators.PRODUCT_TITLE)

    def getCheckoutBtn(self):
        return self.driver.find_element(*HeaderPageLocators.CHECKOUT_BTN)

    def getWelcomeBackBtn(self):
        return self.driver.find_element(*HeaderPageLocators.WELCOMEBACK_BTN)
