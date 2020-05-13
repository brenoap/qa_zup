import pytest
from tests.framework.app import APP
from tests.pages.home.homePage import HomePage
from tests.pages.shopping_cart.shoppingCartPage import ShoppingCartPage
from tests.pages.user_login.userLoginPage import UserLoginPage


@pytest.fixture
def app():
    app = APP()
    yield app


@pytest.fixture
def userLoginPage(app):
    userLoginPage = UserLoginPage(app)
    yield userLoginPage


@pytest.fixture
def homePage(app):
    homePage = HomePage(app)
    yield homePage


@pytest.fixture
def shoppingCartPage(app):
    shoppingCartPage = ShoppingCartPage(app)
    yield shoppingCartPage
