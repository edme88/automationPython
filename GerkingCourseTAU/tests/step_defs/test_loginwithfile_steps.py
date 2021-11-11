from pytest_bdd import scenarios, given, when, then, parsers
import json
from GerkingCourseTAU.Pages.LoginPage import LoginPage

# Scenarios
scenarios('../features/LoginWithFile.feature')


@when('complete user and pass')
def complete_user_pass(browser):
    login_page = LoginPage(browser)
    browser.find_element_by_css_selector('#customer_menu_top > li').click()
    browser.implicitly_wait(100)
    file = open("../../Datos/user_data.json", "r")

    jsondata = file.read()
    obj = json.loads(jsondata)
    list = obj['users']

    login_page.getInputName().send_keys(list[0].get("user"))
    login_page.getInputPassword().send_keys(list[0].get("password"))
    login_page.getBtnLogin().click()


@then("Login correctly")
def check_title(browser):
    assert browser.find_element_by_css_selector('h1 span.maintext').text == 'MY ACCOUNT'


@then("Error in Login")
def check_error_title(browser):
    assert 'Error: Incorrect login or password provided.' in browser.find_element_by_css_selector('div.alert-error').text

#http://thetestingworldapi.com/Help
#https://reqres.in/