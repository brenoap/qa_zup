# coding=utf-8
import time

from tests.framework.app import APP

from tests.pages.homePage import HomePage
from tests.pages.shoppingCartPage import ShoppingCartPage
from tests.pages.userLoginPage import UserLoginPage

app = APP()

userLoginPage = UserLoginPage(app)

homePage = HomePage(app)

shoppingCartPage = ShoppingCartPage(app)

