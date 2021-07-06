import unittest
from selenium.webdriver.common.by import By

class MenuPage(unittest.TestCase):
    MENU = (By.ID, 'categorymenu')
    MENU_HOME = (By.CLASS_NAME, 'menu_home')
    MENU_APPAREL_ACCESSORIES = (By.CSS_SELECTOR, '.categorymenu > li:nth-of-type(2) > a')
    MENU_MAKEUP = (By.CSS_SELECTOR, '.categorymenu > li:nth-of-type(3) > a')
    MENU_SKINCARE = (By.CSS_SELECTOR, '.categorymenu > li:nth-of-type(4) > a')
    MENU_FRAGRANCE = (By.CSS_SELECTOR, '.categorymenu > li:nth-of-type(5) > a')
    MENU_MEN = (By.CSS_SELECTOR, '.categorymenu > li:nth-of-type(6) > a')
    MENU_HAIR_CARE = (By.CSS_SELECTOR, '.categorymenu > li:nth-of-type(7) > a')
    MENU_BOOKS = (By.CSS_SELECTOR, '.categorymenu > li:nth-of-type(8) > a')

    def __init__(self, driver):
        self.driver = driver

    def getMenu(self):
        return self.driver.find_element(*self.MENU)

    def clickMenuHome(self):
        self.driver.find_element(*self.MENU_HOME).click()

    def clickMenuApparelAccessories(self):
        self.driver.find_element(*self.MENU_APPAREL_ACCESSORIES).click()

    def clickMenuMakeUp(self):
        self.driver.find_element(*self.MENU_MAKEUP).click()

    def clickMenuSkinCare(self):
        self.driver.find_element(*self.MENU_SKINCARE).click()

    def clickMenuFragrance(self):
        self.driver.find_element(*self.MENU_FRAGRANCE).click()

    def clickMenuMen(self):
        self.driver.find_element(*self.MENU_MEN).click()

    def clickMenuHairCare(self):
        self.driver.find_element(*self.MENU_HAIR_CARE).click()

    def clickMenuBooks(self):
        self.driver.find_element(*self.MENU_BOOKS).click()
