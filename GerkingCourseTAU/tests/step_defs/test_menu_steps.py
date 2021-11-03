from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage

# Scenarios
scenarios('../features/Menu.feature')


# When Steps
@when(parsers.parse('get options in the menu'))
def get_options_menu(browser):
    header_page = HeaderPage(browser)

    #Search Product and add to card
    menu = header_page.getMenu().text
    print('The menu is: '+menu)


# Then Steps
@then(parsers.parse('option "{num}" is "{option}"'))
def is_ok(browser, num, option):
    header_page = HeaderPage(browser)

    assert option in header_page.getMenuOptions(num).text
    print('Option '+str(num)+' is: '+header_page.getMenuOptions(num).text)
