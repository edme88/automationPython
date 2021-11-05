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
    # move to new tab
    browser.switch_to.window(browser.window_handles[1])

    assert contribute_page.getTitle().text == title
    print('Title is: ' + title)


@then(parsers.parse('the title of the tab is "{tab_title}"'))
def check_tab_title(browser, tab_title):
    assert browser.title == tab_title
    print('The title of the tab is: ' + tab_title)


@then(parsers.parse('the url is "{url_new}"'))
def check_new_url(browser, url_new):
    assert browser.current_url == url_new
    print('The url is: ' + url_new)


