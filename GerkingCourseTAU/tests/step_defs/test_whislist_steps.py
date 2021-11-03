from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from GerkingCourseTAU.Pages.ProductPage import ProductPage
from GerkingCourseTAU.Pages.LoginPage import LoginPage
from GerkingCourseTAU.Pages.WishlistPage import WishlistPage
from GerkingCourseTAU.Pages.AccountPage import AccountPage


# Scenarios
scenarios('../features/Wishlist.feature')


# When Steps
@when(parsers.parse('the user is login with "{user}" and "{password}"'))
def login_user_pass(browser, user, password):
    header_page = HeaderPage(browser)
    login_page = LoginPage(browser)

    header_page.getLoginRegisterBtn().click()
    browser.implicitly_wait(10)
    login_page.getInputName().send_keys(user)
    login_page.getInputPassword().send_keys(password)
    login_page.getBtnLogin().click()
    print('User is Loged in')


@when(parsers.parse('add a "{productName}" to the wishList'))
def add_wish_list(browser, productName):
    header_page = HeaderPage(browser)
    product_page = ProductPage(browser)

    header_page.getSearchInput().send_keys(productName)
    header_page.getSearchButton().click()
    browser.implicitly_wait(10)

    try:
        product_page.getAddToWishlist().click()
    except:
        print('element is added in Wishlist')

    print('Product is search and added to wishlist')


# Then Steps
@then(parsers.parse('the "{productName}" is in the wishlist'))
def product_in_wishlist(browser, productName):
    header_page = HeaderPage(browser)
    wishlist_page = WishlistPage(browser)
    account_page = AccountPage(browser)

    header_page.getWelcomeBackBtn().click()
    account_page.getWishListBtn().click()

    print(wishlist_page.getTableWish().text)
    assert productName in wishlist_page.getTableWish().text
    print(productName+'is in '+wishlist_page.getTableWish().text)
