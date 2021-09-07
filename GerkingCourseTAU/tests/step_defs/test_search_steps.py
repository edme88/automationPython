import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage

# Constants
STORE_HOME = 'https://automationteststore.com/'

# Scenarios
scenarios('../features/Search.feature')

# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps
@given('the search input in the header')
def go_login_page(browser):
    browser.get(STORE_HOME)

@when(parsers.parse('write "{productName}" and press the search button'))
def complete_productName(browser, productName):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(productName)
    header_page.getSearchButton().click()

@then(parsers.parse('See the product "{title}" displayed'))
def check_productTitle(browser, title):
    header_page = HeaderPage(browser)
    assert title in header_page.getProductTitle().text