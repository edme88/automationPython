import unittest
from selenium.webdriver.common.by import By

class MyAccountPage(unittest.TestCase):
    USERNAME = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(*self.USERNAME).text