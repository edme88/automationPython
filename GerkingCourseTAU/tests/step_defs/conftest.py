import pytest
from pytest_bdd import scenarios, given
from selenium import webdriver

# Constants
STORE_HOME = 'https://automationteststore.com/'


# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps
@given('the search input in the header')
@given('the Store webPage', target_fixture='go_home_page')
def go_home_page(browser):
    browser.get(STORE_HOME)
