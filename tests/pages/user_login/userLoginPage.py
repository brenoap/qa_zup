from selenium.webdriver.common.by import By
from tests.locator.locator import Locator
from tests.framework.base_element import BaseElement
from tests.testdata.testrun import TEST_RUN_DATA as test_run_data


class UserLoginPage:

    def __init__(self, app):
        self.driver = app.driver
        self.driver.maximize_window()

    # Locators

    @property
    def email_input(self):
        locator = Locator(By.ID, "email-input")
        return BaseElement(self.driver, locator)

    @property
    def password_input(self):
        locator = Locator(By.ID, "password-input")
        return BaseElement(self.driver, locator)

    @property
    def login_button(self):
        locator = Locator(By.ID, "login-button")
        return BaseElement(self.driver, locator)

    # Methods

    def goToLoginPage(self):
        self.driver.get(test_run_data['login_page_url'])

    def insertEmail(self, text):
        self.email_input.input_text(text)

    def insertPassword(self, text):
        self.password_input.input_text(text)

    def clickOnLogin(self):
        self.login_button.click()
