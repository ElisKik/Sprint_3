"""
Common functions reusable in several tests.
"""

from selenium.webdriver import Chrome as WebDriver

from selenium.common.exceptions import NoSuchElementException

from account import RegisteredAccount
from aliases import Locator
from locators import Locators
from urls import Urls
from waits import wait_click, wait_obscured_click, wait_send_keys, wait_page_loaded

def assert_login(webdriver: WebDriver, registered_account: RegisteredAccount):
    """
    Performs login with given object of registered account.

    Asserts successful login.
    """

    wait_send_keys(webdriver, Locators.Login.INPUT_EMAIL, registered_account.email)
    wait_send_keys(webdriver, Locators.Login.INPUT_PASSWORD, registered_account.password)

    wait_click(webdriver, Locators.Login.BUTTON_LOGIN)

    url_before = webdriver.current_url

    wait_obscured_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)

    url_before_redirect = webdriver.current_url

    if webdriver.current_url == url_before:
        wait_page_loaded(webdriver, url_before)

    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
    url_actual = webdriver.current_url

    # Handle possible redirect from /account to account/profile
    if url_actual == url_before_redirect and not url_before_redirect == url_expected:
        wait_page_loaded(webdriver, url_before_redirect)

    assert webdriver.current_url == url_expected, \
           f'Login with registered account has failed, URL\nexpected: {url_expected},\nactual: {url_actual}'

def assert_element_exists(webdriver: WebDriver, locator: Locator, message: str):
    """
    Checks for element exists and raises exception if not.
    """

    try:
        webdriver.find_element(*locator)
    except NoSuchElementException as exception:
        raise AssertionError(message, exception)
