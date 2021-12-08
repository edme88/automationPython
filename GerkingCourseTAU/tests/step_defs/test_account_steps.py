from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.AccountPage import AccountPage
from selenium.webdriver.common.action_chains import ActionChains


# Scenarios
scenarios('../features/Account.feature')


#Then Steps
@then('all the buttons are grey by default')
def check_button_color_default(browser):
    account_page = AccountPage(browser)

    for i in range(9):
        #light-grey
        assert 'rgb(245, 245, 245)' in account_page.getButton(i+1).value_of_css_property('background-color')

    print('All the button colors by default are checked')


@then('all the button are orange when hover')
def check_button_color_hover(browser):
    account_page = AccountPage(browser)

    for i in range(9):
        #orange
        hover = ActionChains(browser).move_to_element(account_page.getButton(i+1))
        hover.perform()
        assert 'rgb(242, 92, 39)' in account_page.getButton(i+1).value_of_css_property('background-color')

    print('All the button colors hover are checked')
