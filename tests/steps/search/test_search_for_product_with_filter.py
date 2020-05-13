import pytest, time
from tests.framework.fixture import homePage
from tests.framework.fixture import app
from tests.testdata.testrun import TEST_RUN_DATA as test_run_data


from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('../../features/search_for_product.feature', 'Search for a Product using the Filter')
def test_search_for_a_product():
    """Search for a Product"""


@given('Im on Home Page')
def i_am_on_home_page(homePage):
    homePage.goToHomePage()


@when('I search for Galaxy s20')
def i_search_for_galaxy_s20(homePage):
    homePage.searchForProduct(test_run_data['product_name'])


@then('I should see my product on the list')
def i_should_see_my_product_on_the_list(homePage):
    homePage.verifyProductOnList()


@when('I filter by Smartphone')
def i_filter_by_smartphone(homePage):
    homePage.filterSearchByType()


@then('I should open the Product Page')
def i_should_open_the_product_page(homePage, app):
    time.sleep(5)
    homePage.openProductsPage()
    app.take_screenshot('results')
    app.driver.quit()
