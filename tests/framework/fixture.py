import pytest
from tests.framework.app import APP
from tests.pages.homePage import HomePage
from tests.pages.shoppingCartPage import ShoppingCartPage
from tests.pages.userLoginPage import UserLoginPage


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
