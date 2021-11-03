from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.FooterPage import FooterPage
from GerkingCourseTAU.Pages.ContributePage import ContributePage

# Scenarios
scenarios('../features/Contribute.feature')


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


