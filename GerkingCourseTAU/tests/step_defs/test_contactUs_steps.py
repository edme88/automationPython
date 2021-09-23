import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from GerkingCourseTAU.Pages.FooterPage import FooterPage
from GerkingCourseTAU.Pages.ContactUsPage import ContactUsPage

# Constants
STORE_HOME = 'https://automationteststore.com/'

# Scenarios
scenarios('../features/ContactUs.feature')

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
@when('the user access to contactUs section')
def access_contactUs(browser):
    footer_page = FooterPage(browser)

    footer_page.getContactUs().click()
    print('Click Contact Us Btn')


@when(parsers.parse('complete the First name "{name}" Email "{email}" and Enquiry "{message}"'))
def complete_contact_form(browser, name, email, message):
    contact_page = ContactUsPage(browser)

    contact_page.getNameInput().send_keys(name)
    contact_page.getEmailInput().send_keys(email)
    contact_page.getTextInput().send_keys(message)
    contact_page.getSubmitBtn().click()
    print('Complete form and Send')


# Then Steps
@then(parsers.parse('the text "{confirmation}" is displayed'))
def product_in_wishlist(browser, confirmation):
    contact_page = ContactUsPage(browser)

    contact_page.getConfirmationText().text == confirmation
    print('The text '+confirmation+' is displayed')




