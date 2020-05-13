import warnings

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
import os
import json


class BaseElement(object):
    def __init__(self, driver, locator, timeout=5):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.element = None
        self.find_element()

    def find_element(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.visibility_of_element_located(locator=self.locator)
            )
            self.element = element
            return self.element
        except TimeoutException:
            print("\nCould not find element with this locator: {}".format(self.locator))
            return None

    def find_elements(self):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.visibility_of_all_elements_located(locator=self.locator)
            )
            self.element = element
            return self.element
        except TimeoutException:
            print("\nCould not find elements with this locator: {}".format(self.locator))
            return None

    def input_text(self, txt):
        self.element.click()
        self.element.clear()
        self.element.send_keys(txt)

    def press_key(self, key, use_action_chains=False):
        if not use_action_chains:
            self.element.send_keys(key)
        else:
            chains = ActionChains(driver=self.driver)
            chains.send_keys(key).perform()
        return self

    def tap(self):
        element = WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.element_to_be_clickable(locator=self.locator)
        )
        element.click()

    def clear_text(self):
        self.element.click()
        self.element.clear()

    def check_casing(self, string):
        if str(self.text) == string:
            return
        else:
            warnings.warn(UserWarning("WARNING: Element is not in title casing"))

    def wait_while_present(self):
        # Waits a max of 10 seconds for an element that is displayed to disappear (Used for loading wheels)
        WebDriverWait(self.driver, 10).until_not(
            expected_conditions.visibility_of_element_located(locator=self.locator))
        return None

    def is_toggled(self, platform):
        if platform == 'android':
            status = self.element.get_attribute("checked")
            return status == 'true'
        else:
            status = self.element.get_attribute("value")
            return status == '1'

    def exists(self):
        try:
            WebDriverWait(self.driver, 6).until(
                expected_conditions.presence_of_element_located(locator=self.locator))
        except TimeoutException:
            return False
        return True

    def wait_for_element_to_reattach_to_dom(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.staleness_of(self.element))
        except TimeoutException:
            return False
        self.find_element()
        return True


    def wait_to_appear(self, seconds=10, ignore_error=False):
        start = time.time()
        while (time.time() - start) < seconds:
            if self.exists():
                return self
        if not ignore_error:
            raise AssertionError("Locator: {} did not appear in {} seconds!".format(self.locator, seconds))
        else:
            return self

    def is_clickable(self):
        def is_clickable(locator):
            try:
                WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable(locator))
                return True
            except TimeoutException:
                return False

        return self.exists() and is_clickable(self.locator)

    def wait_to_be_clickable(self, seconds=10, ignore_error=False):
        start = time.time()
        while (time.time() - start) < seconds:
            if self.is_clickable():
                return self
            time.sleep(1)
        if not ignore_error:
            if self.exists():
                raise AssertionError("Locator in the DOM: {} but did not become click-able in {} seconds"
                                     .format(self.locator, seconds))
            raise AssertionError("Locator is not in the DOM and so not click-able: {}".format(self.locator))
        else:
            return self

    def wait_to_be_disabled(self, seconds=10):
        elem = self.element
        start = time.time()
        while (time.time() - start) < seconds:
            if not elem.is_enabled():
                return True
            time.sleep(1)
        return False

    def wait_to_be_visible(self, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(
                expected_conditions.visibility_of(self.element)
            )
        except TimeoutException:
            return None

    def get_attribute(self, value):
        return self.element.get_attribute(value)

    def click(self, wait=10):
        self.wait_to_be_clickable(wait)
        self.find_element().click()

    def clear_textbox(self):
        self.input_text("")

    def select_drop_down_by_index(self, index):
        try:
            Select(self.element).select_by_index(index)
        except ElementNotSelectableException as err:
            print(err)

    def select_drop_down_by_value(self, value):
        try:
            Select(self.element).select_by_value(value)
        except ElementNotSelectableException as err:
            print(err)

    def select_drop_down_by_visible_text(self, text):
        try:
            Select(self.element).select_by_visible_text(text)
        except ElementNotSelectableException as err:
            print(err)

    def get_all_options_from_drop_down_list(self):
        option_list = []
        try:
            for i in Select(self.element).options:
                option_list.append(i.text)
        except ElementNotSelectableException as err:
            print(err)
        return option_list

    @property
    def text(self):
        if self.element is None:
            self.find_element()
        return self.element.text

    @property
    def x(self):
        return self.element.location['x']

    @property
    def y(self):
        return self.element.location['y']

    @property
    def width(self):
        return self.element.size['width']

    @property
    def height(self):
        return self.element.size['height']

    def scroll_into_center(self):
        scroll_element_into_middle = "var viewPortHeight = Math.max(document.documentElement.clientHeight, " \
                                     "window.innerHeight || 0); " \
                                     "var elementTop = arguments[0].getBoundingClientRect().top; " \
                                     "window.scrollBy(0, elementTop-(viewPortHeight/2));"

        self.driver.execute_script(scroll_element_into_middle, self.find_element())

    def scroll_into_view(self):
        scroll_into_view = "arguments[0].scrollIntoView(true);"
        self.driver.execute_script(scroll_into_view, self.element)

    def checkbox_click(self):
        self.scroll_into_view()
        sc = "arguments[0].click();"
        self.driver.execute_script(sc, self.element)

    def switch_to_latest_active_window(self):
        windows = self.driver.window_handles
        if len(windows) == 1:
            self.driver.switch_to.window(windows[0])
            return
        for index in range(1, len(windows)):
            self.driver.switch_to.window(windows[-index])
            return

    def find_elements_by_xpath(self, xpath):
        try:
            return self.element.find_elements_by_xpath(xpath)
        except ElementNotSelectableException as err:
            print(err)

    def find_elements_by_tag_name(self, tag_name):
        try:
            return self.element.find_elements(By.TAG_NAME, tag_name)
        except ElementNotSelectableException as err:
            print(err)

    def find_elements_by_class_name(self, class_name):
        try:
            return self.element.find_elements(By.CLASS_NAME, class_name)
        except ElementNotSelectableException as err:
            print(err)
