from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.locator.locator import Locator
from tests.framework.base_element import BaseElement
from tests.testdata.testrun import TEST_RUN_DATA as test_run_data


class HomePage:

    def __init__(self, app):
        self.driver = app.driver
        self.driver.maximize_window()

# Locators

    @property
    def search_bar(self):
        locator = Locator(By.ID, "h_search-input")
        return BaseElement(self.driver, locator)

    @property
    def search_filter(self):
        locator = Locator(By.XPATH, "//*[@id='collapse-categorias']/ul/li[1]/a/span")
        return BaseElement(self.driver, locator)

    @property
    def home_page_title(self):
        locator = Locator(By.ID, "brd-title")
        return BaseElement(self.driver, locator)

    @property
    def item_list(self):
        locator = Locator(By.XPATH, "//*[@id='content-middle']/div["
                                    "6]/div/div/div/div[1]/div[2]/div/div["
                                    "2]/a/section/div[2]/div[1]/h2")
        return BaseElement(self.driver, locator)

# Methods

    def goToHomePage(self):
        self.driver.get(test_run_data['home_page_url'])

    def checkHomePage(self):
        self.home_page_title.exists()

    def searchForProduct(self, text):
        self.search_bar.input_text(text)
        self.search_bar.press_key(Keys.RETURN)

    def filterSearchByType(self):
        self.search_filter.click()

    def verifyProductOnList(self):
        self.item_list.exists()

    def openProductsPage(self):
        self.item_list.wait_to_be_visible()
        self.item_list.click()
