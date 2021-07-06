from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

import time
from Store.Pages.IndexPage import IndexPage
from Store.Pages.LoginOrRegister import LoginOrRegisterPage
from Store.Pages.CreateAccountPage import CreateAccountPage
import HtmlTestRunner

class registerTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("../../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://automationteststore.com/")
        cls.driver.maximize_window()

    def test_registration_fields_incomplete(self):
        index_page = IndexPage(self.driver)
        login_page = LoginOrRegisterPage(self.driver)
        create_account = CreateAccountPage(self.driver)

        ## Step 1: Click Button Login or Register
        index_page.goToLoginOrRegisterPage()
        time.sleep(2)

        ## Step 2: Select Register
        login_page.continueToRegister()
        time.sleep(2)

        ## Step 3: Click continue Button
        create_account.clickContinueBtn()

        ## Step 4: Check Error Messages from each field
        print(create_account.checkErrorMsgFirstName())
        assert create_account.checkErrorMsgFirstName() == 'First Name must be between 1 and 32 characters!'

        print(create_account.checkErrorMsgLastName())
        assert create_account.checkErrorMsgLastName() == 'Last Name must be between 1 and 32 characters!'

        print(create_account.checkErrorMsgEmail())
        assert create_account.checkErrorMsgEmail() == 'Email Address does not appear to be valid!'

        print(create_account.checkErrorMsgAddress())
        assert create_account.checkErrorMsgAddress() == 'Address 1 must be between 3 and 128 characters!'

        print(create_account.checkErrorMsgCity())
        assert create_account.checkErrorMsgCity() == 'City must be between 3 and 128 characters!'

        print(create_account.checkErrorMsgState())
        assert create_account.checkErrorMsgState() == 'Please select a region / state!'

        print(create_account.checkErrorMsgZipCode())
        assert create_account.checkErrorMsgZipCode() == 'Zip/postal code must be between 3 and 10 characters!'

        print(create_account.checkErrorMsgLogin())
        assert create_account.checkErrorMsgLogin() == 'Login name must be alphanumeric only and between 5 and 64 characters!'

        print(create_account.checkErrorMsgPassword())
        assert create_account.checkErrorMsgPassword() == 'Password must be between 4 and 20 characters!'

        print('TEST: CREATE ACCOUNT PAGE - Check message error from each field')

    def test_registration_fail_alredy_register(self):
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
        create_account.login('agusDarwoft', 'automation', 'automation')
        assert 'Error: E-Mail Address is already registered!' in create_account.checkErrorMsg()
        print('TEST: CREATE ACCOUNT PAGE - Check message error: Account Alredy Exist')

    def test_registration_checkLongText(self):
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
        create_account.personalDetails('a', 'a', 'a@a.com', '', '')
        create_account.addressDetails('', 'aaa', '', 'aaa', 'aaa', 'aaa', '')
        create_account.login('aaaaa', 'aaaa', 'aaab', False, False)
        assert 'Error: You must agree to the Privacy Policy!' in create_account.checkErrorMsg()
        print(create_account.checkErrorMsg())
        assert create_account.checkErrorMsgFirstName() == ''
        assert create_account.checkErrorMsgLastName() == ''
        assert create_account.checkErrorMsgEmail() == ''
        assert create_account.checkErrorMsgAddress() == ''
        assert create_account.checkErrorMsgCity() == ''
        assert create_account.checkErrorMsgState() == ''
        assert create_account.checkErrorMsgZipCode() == ''
        assert create_account.checkErrorMsgLogin() == 'This login name is not available. Try different login name!'
        print(create_account.checkErrorMsgLogin())
        assert create_account.checkErrorMsgPasswordConfirm() == 'Password confirmation does not match password!'
        print(create_account.checkErrorMsgPasswordConfirm())
        print('TEST: CREATE ACCOUNT PAGE - Long text - Check message error: login name not available & password not match')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/"), verbosity=2)