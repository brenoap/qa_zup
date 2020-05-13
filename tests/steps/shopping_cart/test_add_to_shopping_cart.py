import pytest
from tests.framework.fixture import shoppingCartPage
from tests.framework.fixture import app
from tests.testdata.testrun import TEST_RUN_DATA as test_run_data


from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('./../../features/shopping_cart/add_to_shopping_cart.feature', 'I buy a Product')
def test_i_buy_a_product():
    """I buy a Product"""


@given('Im at Product Page')
def i_am_on_home_page(shoppingCartPage):
    shoppingCartPage.goToProductPage(test_run_data['product_id'])


@when('I click on add to shopping cart')
def i_click_on_add_to_shopping_cart(shoppingCartPage):
    shoppingCartPage.buyProduct()


@when('I go to Shopping Cart Page')
def i_go_to_shopping_cart_page(shoppingCartPage):
    assert(shoppingCartPage.verifyShoppingCartPage())


@then('Verify that my Product is on the Basket')
def verify_that_my_product_is_on_the_basket(shoppingCartPage, app):
    assert(shoppingCartPage.verifyProductOnBasket())
    app.take_screenshot('results')
    app.driver.quit()
