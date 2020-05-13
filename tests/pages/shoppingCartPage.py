import re
import time

from selenium.webdriver.common.by import By

from tests.framework.base_element import BaseElement
from tests.locator.locator import Locator
from tests.testdata.testrun import TEST_RUN_DATA as test_run_data


class ShoppingCartPage:

    def __init__(self, app):
        self.driver = app.driver
        self.driver.maximize_window()

    def goToProductPage(self, PRODUCT_CODE):
        self.driver.get("https://www.shoptime.com.br/produto/" + PRODUCT_CODE)

    def goToShoppingCarPage(self):
        self.driver.get("https://sacola.shoptime.com.br/simple-basket")

    @property
    def buy_button(self):
        locator = Locator(By.ID, "btn-buy")
        return BaseElement(self.driver, locator)

    @property
    def remove_product(self):
        locator = Locator(By.CLASS_NAME, "basket-productRemoveAct")
        return BaseElement(self.driver, locator)

    def buyProduct(self):
        self.buy_button.click()

    def verifyShoppingCartPage(self):
        src = self.driver.page_source
        text_found = re.search(r'Meu carrinho', src)
        return text_found

    def verifyProductOnBasket(self):
        src = self.driver.page_source
        text_found = re.search(r'Smartphone Samsung Galaxy S20', src)
        return text_found

    def verifyEmptyBasket(self):
        time.sleep(3)
        src = self.driver.page_source
        text_found = re.search(r'Seu carrinho está vazio', src)
        return text_found

    def removeProductFromBasket(self):
        self.remove_product.click()
