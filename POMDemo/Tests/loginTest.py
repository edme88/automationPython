import time
import unittest
from selenium import webdriver
from POMDemo.Pages.IndexPage import IndexPage
from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.MyAccountPage import MyAccountPage


class loginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../../Drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/")
        self.driver.fullscreen_window()

    def test_invalid_login(self):
        index_page = IndexPage(self.driver)
        login_page = LoginPage(self.driver)
        my_account_page = MyAccountPage(self.driver)

        ## Step 1: Select sign in button
        index_page.goToLoginPage()
        time.sleep(2)

        ## Step 2: Comple user and pass
        login_page.login('myUsu@email.com', 'papafrita')

        ## Step 3: Check error
        time.sleep(10)
        assert login_page.checkError1() == 'There is 1 error'
        assert 'There is 1 error' in login_page.checkError1()
        self.assertIn('There is 1 error', login_page.checkError1())
        assert login_page.checkError2() == 'Authentication failed.'
