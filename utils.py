"""
Common functions reusable in several tests.
"""

from selenium.webdriver import Chrome as WebDriver

from account import RegisteredAccount
from fakes import get_name, get_email, get_password
from locators import Locators
from urls import Urls
from waits import wait_click, wait_page_loaded

def register_account(webdriver: WebDriver) -> RegisteredAccount:
    """
    Returns object with random fake credentials and real name of user.

    Performs registration on target site.
    """

    name = get_name()
    email = get_email()
    password = get_password()

    webdriver.get(Urls.BASE)

    webdriver.find_element(*Locators.Main.ANCHOR_ACCOUNT).click()
    webdriver.find_element(*Locators.Account.ANCHOR_REGISTER).click()

    webdriver.find_element(*Locators.Registration.INPUT_NAME).send_keys(name)
    webdriver.find_element(*Locators.Registration.INPUT_EMAIL).send_keys(email)
    webdriver.find_element(*Locators.Registration.INPUT_PASSWORD).send_keys(password)

    url_before = webdriver.current_url

    webdriver.find_element(*Locators.Registration.BUTTON_REGISTER).click()

    if webdriver.current_url == url_before:
        wait_page_loaded(webdriver, url_before)

    return RegisteredAccount(name, email, password)

def login(webdriver: WebDriver, registered_account: RegisteredAccount):
    """
    Performs login with given object of registered account.
    """

    webdriver.find_element(*Locators.Login.INPUT_EMAIL).send_keys(registered_account.email)
    webdriver.find_element(*Locators.Login.INPUT_PASSWORD).send_keys(registered_account.password)

    wait_click(webdriver, Locators.Login.BUTTON_LOGIN)

    url_before = webdriver.current_url

    wait_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)

    url_before_redirect = webdriver.current_url

    if webdriver.current_url == url_before:
        wait_page_loaded(webdriver, url_before)

    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
    url_actual = webdriver.current_url

    # Handle possible redirect from /account to account/profile
    if url_actual == url_before_redirect and not url_before_redirect == url_expected:
        wait_page_loaded(webdriver, url_before_redirect)
