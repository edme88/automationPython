import time
import unittest
from selenium import webdriver
from Store.Pages.IndexPage import IndexPage
from Store.Pages.LoginOrRegister import LoginOrRegisterPage
from Store.Pages.CreateAccountPage import CreateAccountPage

class registerTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../../Drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://automationteststore.com/")
        self.driver.fullscreen_window()

    def test_registration(self):
        index_page = IndexPage(self.driver)
        login_page = LoginOrRegisterPage(self.driver)
        create_account = CreateAccountPage(self.driver)

        ## Step 1: Click Button Login or Register
        index_page.goToLoginOrRegisterPage()
        time.sleep(2)

        ## Step 2: Select Register
        login_page.continueToRegister()
        time.sleep(2)

        ## Step 3: Complete Register Information
        create_account.personalDetails('Agus', 'Alici', 'agustina.aliciardi@darwoft.com', '358 4256985', '358 4256985')
        create_account.addressDetails('Darwoft', 'Jujuy 1214', 'West Loop South', 'Cordoba', 'Cordoba', '5000', 'Argentina')
        create_account.login('agusDarwoft', 'automation')
        time.sleep(2000)