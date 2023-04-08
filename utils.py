"""
Common functions reusable in several tests.
"""

from selenium.webdriver import Chrome as WebDriver

from account import RegisteredAccount
from fakes import get_name, get_email, get_password
from javascript import js_click
from locators import Locators
from urls import Urls
from waits import wait_page_loaded, wait_send_keys

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
