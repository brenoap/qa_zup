import pytest
from tests.framework.fixture import userLoginPage
from tests.framework.fixture import app
from tests.testdata.testrun import TEST_RUN_DATA as test_run_data

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('../../features/user_login.feature', 'Login into Shoptime Site')
def test_login_into_shoptime_site():
    """Login into Shoptime Site"""


@given('Im on Login Page')
def iam_on_login_page(userLoginPage):
    userLoginPage.goToLoginPage()


@when('I insert my credentials')
def i_enter_my_credentials(userLoginPage):
    userLoginPage.insertEmail(test_run_data['user_email'])
    userLoginPage.insertPassword(test_run_data['user_password'])


@then('I click on continue button')
def i_click_on_continue_button(userLoginPage, app):
    userLoginPage.clickOnLogin()
    app.take_screenshot('results')
    app.driver.quit()
