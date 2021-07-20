from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

import time
from Store.Pages.IndexPage import IndexPage
from Store.Pages.LoginOrRegister import LoginOrRegisterPage
from Store.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner
import json

class loginTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("../../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://automationteststore.com/")
        cls.driver.maximize_window()

    def test_invalid_login_noUser_noPass(self):
        index_page = IndexPage(self.driver)
        login_page = LoginOrRegisterPage(self.driver)

        ## Step 1: Click Button Login or Register
        index_page.goToLoginOrRegisterPage()
        time.sleep(2)

        ## Step 2: Complete user and pass
        login_page.login('', '')

        ## Step 3: Invalid Login, no login and pass
        assert 'Error: Incorrect login or password provided.' in login_page.checkErrorMsg()
        print('TEST: Invalid Login - No User - No Pass')

    def test_login(self):
        index_page = IndexPage(self.driver)
        login_page = LoginOrRegisterPage(self.driver)
        myAccount_page = MyAccountPage(self.driver)

        ## Step 1: Click Button Login or Register
        index_page.goToLoginOrRegisterPage()
        time.sleep(2)

        ## Step 2: Complete user and pass
        #login_page.login('agusDarwoft', 'automation')
        f = open('../Data/UserData.json',)
        data = json.load(f)
        login_page.login(data["name"], data["password"])

        ## Step 3: Check My Account Page
        assert myAccount_page.checkTitle() == 'MY ACCOUNT'
        print('TEST: Valid Login - Check My Account title')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/"), verbosity=2)