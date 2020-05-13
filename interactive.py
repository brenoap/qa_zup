# coding=utf-8

from tests.framework.app import APP

from tests.pages.home.homePage import HomePage
from tests.pages.shopping_cart.shoppingCartPage import ShoppingCartPage
from tests.pages.user_login.userLoginPage import UserLoginPage

app = APP()

userLoginPage = UserLoginPage(app)

homePage = HomePage(app)

shoppingCartPage = ShoppingCartPage(app)

