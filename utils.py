"""
Common functions reusable in several tests.
"""

from selenium.webdriver import Chrome as WebDriver

from account import RegisteredAccount
from fakes import get_name, get_email, get_password
from javascript import js_click
from locators import Locators
from urls import Urls
from waits import wait_page_loaded, wait_send_keys, wait_click, wait_obscured_click, wait_send_keys, wait_page_loaded

def register_account(webdriver: WebDriver) -> RegisteredAccount:
    """
    Returns object with random fake credentials and real name of user.

    Performs registration on target site.
    """

    name = get_name()
    email = get_email()
    password = get_password()

    webdriver.get(Urls.BASE)

    js_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
    js_click(webdriver, Locators.Account.ANCHOR_REGISTER)

    wait_send_keys(webdriver, Locators.Registration.INPUT_NAME, name)
    wait_send_keys(webdriver, Locators.Registration.INPUT_EMAIL, email)
    wait_send_keys(webdriver, Locators.Registration.INPUT_PASSWORD, password)

    url_before = webdriver.current_url

    js_click(webdriver, Locators.Registration.BUTTON_REGISTER)

    if webdriver.current_url == url_before:
        wait_page_loaded(webdriver, url_before)

    return RegisteredAccount(name, email, password)

def login(webdriver: WebDriver, registered_account: RegisteredAccount):
    """
    Performs login with given object of registered account.
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
