import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from GerkingCourseTAU.Pages.SearchPage import SearchPage
from selenium.webdriver.common.keys import Keys

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

# When Steps
@when(parsers.parse('write "{productName}" and press the search button'))
def complete_productName(browser, productName):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(productName)
    header_page.getSearchButton().click()

@when(parsers.parse('write "{productName}" and press enter'))
def complete_productName(browser, productName):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(productName+Keys.ENTER)

# Then Steps
@then(parsers.parse('See the product "{title}" displayed'))
def check_productTitle(browser, title):
    header_page = HeaderPage(browser)
    assert title in header_page.getProductTitle().text
    print(header_page.getProductTitle().text)

@then(parsers.parse('See the text "{text}" displayed'))
def check_productNotFound(browser, text):
    searchPage = SearchPage(browser)
    assert text in searchPage.getSearchText().text
    print(searchPage.getSearchText().text)


