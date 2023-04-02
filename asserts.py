"""
Common functions reusable in several tests.
"""

from selenium.webdriver import Chrome as WebDriver
from selenium.common.exceptions import NoSuchElementException

from locators import *
from waits import *
from javascript import *
from constants import *
from utils import *

from account import RegisteredAccount
from aliases import Locator

def assert_login(webdriver: WebDriver, registered_account: RegisteredAccount):
    """
    Performs login with given object of registered account.

    Asserts successful login.
    """
    js_send_keys_focused(webdriver, Locators.Login.INPUT_EMAIL, registered_account.email)
    js_send_keys_focused(webdriver, Locators.Login.INPUT_PASSWORD, registered_account.password)

    js_click(webdriver, Locators.Login.BUTTON_LOGIN)

    wait_overlay_hidden(webdriver)

    js_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)

    wait_overlay_hidden(webdriver)

    assert webdriver.current_url == f'{BASE_URL}/account/profile', \
           'Login with registered account has failed'

def assert_element_exists(webdriver: WebDriver, locator: Locator, message: str):
    try:
        webdriver.find_element(*locator)
    except NoSuchElementException as exception:
        raise AssertionError(message, exception)
