import time
import unittest
from selenium import webdriver
from Store.Pages.IndexPage import IndexPage
from Store.Pages.LoginOrRegister import LoginOrRegisterPage

class loginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../../Drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://automationteststore.com/")
        self.driver.fullscreen_window()

    def test_login(self):
        index_page = IndexPage(self.driver)
        login_page = LoginOrRegisterPage(self.driver)

        ## Step 1: Click Button Login or Register
        index_page.goToLoginOrRegisterPage()
        time.sleep(2)

        ## Step 2: Complete user and pass
        login_page.login('agustina.aliciardi@darwoft.com', 'automation')