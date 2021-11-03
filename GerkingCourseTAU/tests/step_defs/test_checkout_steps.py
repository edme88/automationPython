from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from GerkingCourseTAU.Pages.ProductPage import ProductPage
from GerkingCourseTAU.Pages.LoginPage import LoginPage
from GerkingCourseTAU.Pages.CheckoutPage import CheckoutPage
from GerkingCourseTAU.Pages.ConfirmationPage import ConfirmationPage
from GerkingCourseTAU.Pages.AccountPage import AccountPage
import re


# Scenarios
scenarios('../features/Checkout.feature')


# When Steps
@when(parsers.parse('complete a buy transaction with the user "{userName}" and "{password}"'))
def complete_productName(browser, userName, password):
    header_page = HeaderPage(browser)
    product_page = ProductPage(browser)
    login_page = LoginPage(browser)
    checkout_page = CheckoutPage(browser)

    #Search Product and add to card
    header_page.getSearchInput().send_keys('shampoo')
    header_page.getSearchButton().click()
    product_page.getAddToCard().click()
    #Go to checkout and login
    header_page.getCheckoutBtn().click()
    login_page.getInputName().send_keys(userName)
    login_page.getInputPassword().send_keys(password)
    login_page.getBtnLogin().click()
    checkout_page.getBtnConfirmOrder().click()


# Then Steps
@then(parsers.parse('can check if the order ID is present in the history'))
def check_orderID(browser):
    header_page = HeaderPage(browser)
    account_page = AccountPage(browser)
    confirmation_page = ConfirmationPage(browser)

    ##Obtain order id
    orderTxt = confirmation_page.getOrderText().text
    orderN = re.findall("[0-9]", orderTxt)
    print(orderN)
    orderID = ''.join(orderN)
    print(orderID)

    header_page.getWelcomeBackBtn().click()
    header_page.getWelcomeBackBtn().click()
    browser.implicitly_wait(10)
    account_page.getOrderHistoryBtn().click()
    browser.implicitly_wait(10)
    lastOrderTxt = account_page.getLastOrder().text
    print(lastOrderTxt)
    assert orderID in lastOrderTxt

