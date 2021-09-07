import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HeaderPageLocators():
    SEARCH_INPUT = (By.ID, 'filter_keyword')
    SEARCH_BTN = (By.CLASS_NAME, 'fa-search')
    PRODUCT_TITLE = (By.CLASS_NAME, 'bgnone')


class HeaderPage():

    def __init__(self, driver):
        self.driver = driver

    def getSearchInput(self):
        return self.driver.find_element(*HeaderPageLocators.SEARCH_INPUT)

    def getSearchButton(self):
        return self.driver.find_element(*HeaderPageLocators.SEARCH_BTN)

    def getProductTitle(self):
        return self.driver.find_element(*HeaderPageLocators.PRODUCT_TITLE)
