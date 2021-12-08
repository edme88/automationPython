from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.LoginPage import LoginPage
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage

# Scenarios
scenarios('../features/Login.feature')


@when('press Forgot login option')
def press_forgot_option(browser):
    header_page = HeaderPage(browser)
    login_page = LoginPage(browser)

    header_page.getLoginRegisterBtn().click()
    login_page.getForgotLoginLink().click()


@when(parsers.parse('complete with lastname "{lastname}" and email "{email}"'))
def complete_forgot_login(browser, lastname, email):
    login_page = LoginPage(browser)

    login_page.getLastNameInput().send_keys(lastname)
    login_page.getEmailInput().send_keys(email)
    login_page.getContinueButton().click()


@then("Error in Login")
def check_error_title(browser):
    assert 'Error: Incorrect login or password provided.' in browser.find_element_by_css_selector('div.alert-error').text


@then(parsers.parse('Error "{message}" is displayed'))
def check_error_message(browser, message):
    login_page = LoginPage(browser)

    assert message in login_page.getErrorMsg().text


@then(parsers.parse('Message "{message}" is displayed'))
def check_ok_message(browser, message):
    login_page = LoginPage(browser)

    assert message in login_page.getOkMsg().text

#http://thetestingworldapi.com/Help
#https://reqres.in/