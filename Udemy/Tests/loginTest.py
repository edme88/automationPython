import time
import unittest
from selenium import webdriver
from Udemy.Pages.IndexPage import IndexPage
from Udemy.Pages.LoginPage import LoginPage
from Udemy.Pages.MyAccountPage import MyAccountPage


class loginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../../Drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/")
        self.driver.fullscreen_window()

    def test_invalid_username_password(self):
        index_page = IndexPage(self.driver)
        login_page = LoginPage(self.driver)

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
        print("Test 1: Authentication failed. (invalid username or password)")

    def test_invalid_without_username_password(self):
        index_page = IndexPage(self.driver)
        login_page = LoginPage(self.driver)

        ## Step 1: Select sign in button
        index_page.goToLoginPage()
        time.sleep(2)

        ## Step 2: Comple user and pass
        login_page.login('', '')

        ## Step 3: Check error
        time.sleep(10)
        assert login_page.checkError1() == 'There is 1 error'
        assert 'There is 1 error' in login_page.checkError1()
        self.assertIn('There is 1 error', login_page.checkError1())
        assert login_page.checkError2() == 'An email address required.'
        print("Test 2: Email is required")

    def test_invalid_without_password(self):
        index_page = IndexPage(self.driver)
        login_page = LoginPage(self.driver)

        ## Step 1: Select sign in button
        index_page.goToLoginPage()
        time.sleep(2)

        ## Step 2: Comple user and pass
        login_page.login('agustina.aliciardi@darwoft.com', '')

        ## Step 3: Check error
        time.sleep(10)
        assert login_page.checkError1() == 'There is 1 error'
        assert 'There is 1 error' in login_page.checkError1()
        self.assertIn('There is 1 error', login_page.checkError1())
        assert login_page.checkError2() == 'Password is required.'
        print("Test 3: Password is required")

    def test_valid_login(self):
        index_page = IndexPage(self.driver)
        login_page = LoginPage(self.driver)
        my_account_page = MyAccountPage(self.driver)

        ## Step 1: Select sign in button
        index_page.goToLoginPage()
        time.sleep(2)

        ## Step 2: Comple user and pass
        login_page.login('anto_m5@hotmail.com', 'antito')

        ## Step 3: Check username
        time.sleep(10)
        assert my_account_page.get_title() == 'Antonella Morano'
        print("Test 4: Valid Login")

    def test_try_create_account(self):
        index_page = IndexPage(self.driver)
        login_page = LoginPage(self.driver)

        ## Step 1: Select sign in button
        index_page.goToLoginPage()
        time.sleep(2)

        ## Step 2: Comple user and pass
        login_page.createAccount('agustina.aliciardi@darwoft.com')
        time.sleep(2)

        ## Step 3: Check error
        time.sleep(10)
        assert login_page.checkError3() == 'An account using this email address has already been registered. Please enter a valid password or request a new one.'
        print("Test 5: Cannot create account")