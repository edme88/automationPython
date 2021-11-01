import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from GerkingCourseTAU.Pages.ProductPage import ProductPage
from GerkingCourseTAU.Pages.LoginPage import LoginPage
from GerkingCourseTAU.Pages.CheckoutPage import CheckoutPage
from GerkingCourseTAU.Pages.ConfirmationPage import ConfirmationPage
from GerkingCourseTAU.Pages.AccountPage import AccountPage
import re

# Constants
STORE_HOME = 'https://automationteststore.com/'

# Scenarios
scenarios('../features/Menu.feature')

# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps
@given('the Store webPage')
def go_login_page(browser):
    browser.get(STORE_HOME)

# When Steps
@when(parsers.parse('get options in the menu'))
def get_options_menu(browser):
    header_page = HeaderPage(browser)

    #Search Product and add to card
    menu = header_page.getMenu().text
    print('The menu is: '+menu)


# Then Steps
@then(parsers.parse('option "{num}" is "{option}"'))
def is_ok(browser, num, option):
    header_page = HeaderPage(browser)

    assert option in header_page.getMenuOptions(num).text
    print('Option '+str(num)+' is: '+header_page.getMenuOptions(num).text)
