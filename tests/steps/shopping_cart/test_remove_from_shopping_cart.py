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


@scenario('../../features/remove_from_shopping_cart.feature', 'I decide not to buy the Product')
def test_i_decide_not_to_buy_the_product():
    """I decide not to buy the Product"""


@given('Im on Product Page')
def i_am_on_product_page(shoppingCartPage):
    shoppingCartPage.goToProductPage(test_run_data['product_id'])


@when('I click on add to shopping cart')
def i_click_on_add_to_shopping_cart(shoppingCartPage):
    shoppingCartPage.buyProduct()


@then('I verify my product on Basket')
def i_verify_my_product_on_basket(shoppingCartPage):
    assert (shoppingCartPage.verifyProductOnBasket())


@then('Decide to remove the Product')
def decide_to_remove_the_product(shoppingCartPage):
    shoppingCartPage.removeProductFromBasket()


@then('Verify that my Product is on the Basket')
def verify_that_my_product_is_on_the_basket(shoppingCartPage, app):
    assert shoppingCartPage.verifyEmptyBasket()
    app.take_screenshot('results')
    app.driver.quit()
