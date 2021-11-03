import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from GerkingCourseTAU.Pages.FooterPage import FooterPage
from GerkingCourseTAU.Pages.ContributePage import ContributePage

# Constants
STORE_HOME = 'https://automationteststore.com/'

# Scenarios
scenarios('../features/Contribute.feature')

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
    print('Browser is open')

# When Steps
@when('press contribute button')
def access_contactUs(browser):
    footer_page = FooterPage(browser)

    footer_page.getContribute().click()
    print('Click Contribute Btn')


@then(parsers.parse('the title "{title}" is displayed in the new page'))
def complete_contact_form(browser, title):
    contribute_page = ContributePage(browser)
    browser.switch_to.window(browser.window_handles[1])

    assert contribute_page.getTitle().text == title
    print('Title is: ' + title)


