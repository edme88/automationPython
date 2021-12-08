from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from GerkingCourseTAU.Pages.ListOfProductsPage import ListOfProductsPage


# Scenarios
scenarios('../features/Special.feature')


# When Steps
@when('press special button')
def press_special_button(browser):
    header_page = HeaderPage(browser)

    header_page.getSpecialBtn().click()
    print('Click Special button')


@then('all the offers are displayed with the flag Sale')
def flag_sale_displayed(browser):
    list_product_page = ListOfProductsPage(browser)

    for i in range(len(list_product_page.getProductCard())+1):
        if i != 4:
            assert list_product_page.getSaleNum(i + 1).is_displayed() is True
            print('Sale ' + str(i + 1) + ' is displayed')



    print('All the sales banners are displayed')
