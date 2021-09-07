import unittest
from selenium.webdriver.common.by import By

class MakeUpPage(unittest.TestCase):
    VIVA_GLAM_LIPSTICK = (By.CSS_SELECTOR, 'div.list-inline div:nth-child(7)>div.thumbnail')

    def __init__(self, driver):
        self.driver = driver

    def getVivaGlamLipStick(self):
        return self.driver.find_element(*self.VIVA_GLAM_LIPSTICK).click()