import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from GerkingCourseTAU.Pages.ProductPage import ProductPage
from selenium.webdriver.common.keys import Keys

# Constants
STORE_HOME = 'https://automationteststore.com/'

# Scenarios
scenarios('../features/Product.feature')

# Fixtures
@pytest.fixture
def browser():
    #b = webdriver.Firefox()
    b = webdriver.Chrome(executable_path='../../../Drivers/chromedriver.exe')
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps
@given('the Store webPage')
def go_homepage(browser):
    browser.get(STORE_HOME)


# When Steps
@when(parsers.parse('write "{product_name}" and press the search button'))
def complete_productName_in_search(browser, product_name):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(product_name)
    header_page.getSearchButton().click()
    print('Search Product')


@then(parsers.parse('download PDF'))
def product_PDF(browser):
    productPage = ProductPage(browser)

    productPage.getPrintBtn().click()
    #productPage.getSaveBtn().click()
    print('Press print Button')


@then('check that Out of Stock is visible')
def out_of_stock(browser):
    productPage = ProductPage(browser)

    assert productPage.getOutStock().is_displayed() == True
    print('Out Stock is visible')
    print(productPage.getOutStock().value_of_css_property('background'))
    assert 'rgb(204, 204, 204)' in productPage.getOutStock().value_of_css_property('background')


@then('add to cart is not visible')
def add_to_cart_not_visible(browser):

    try:
        element = browser.find_element_by_css_selector('ul.productpagecart a')
        print('Add to cart is visible')
    except NoSuchElementException:
        print('Add to cart is NOT visible')
