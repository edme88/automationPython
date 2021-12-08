from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.HomePage import HomePage
from GerkingCourseTAU.Pages.ListOfProductsPage import ListOfProductsPage
import json
import time


# Scenarios
scenarios('../features/Banner.feature')


# When Steps
@when('see the banner', target_fixture='get_banner_info')
def get_banner_info(browser):
    home_page = HomePage(browser)

    home_page.getBanner().get_attribute("src")
    print('Actual banner')


@then('check the information displayed')
def banner_image(browser, get_banner_info):
    home_page = HomePage(browser)

    file = open('../../Datos/banner.json', "r")
    data = file.read()
    obj = json.loads(data)
    list = obj['banners']
    print('Unordered list: ')
    print(list)


    for i in range(len(list)):
        image = list[i].get("image")
        print('Image from array: '+image)
        time.sleep(25)
        print('Image from page: '+home_page.getBannerImage().get_attribute("src"))
        assert image in home_page.getBannerImage().get_attribute("src")

    print('Banner is checked')
