import pytest
from pytest_bdd import given, when, then, parsers
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


@when(parsers.parse('complete "{user}" and "{password}"'))
def complete_user_pass(browser, user, password):
    browser.find_element_by_css_selector('#customer_menu_top > li').click()
    browser.implicitly_wait(100)
    browser.find_element_by_id('loginFrm_loginname').send_keys(user)
    browser.find_element_by_id('loginFrm_password').send_keys(password)
    browser.find_element_by_css_selector('button[title="Login"]').click()


@when("Login correctly")
@then("Login correctly")
def check_title(browser):
    assert browser.find_element_by_css_selector('h1 span.maintext').text == 'MY ACCOUNT'
