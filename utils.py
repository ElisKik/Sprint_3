"""
Common functions reusable in several tests.
"""

from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from account import RegisteredAccount
from constants import TIMEOUT
from fakes import get_name, get_email, get_password
from locators import Locators
from urls import Urls

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
        wait = WebDriverWait(webdriver, TIMEOUT)
        wait.until(expected_conditions.url_changes(url_before))

    return RegisteredAccount(name, email, password)

def login(webdriver: WebDriver, registered_account: RegisteredAccount):
    """
    Performs login with given object of registered account.
    """

    webdriver.find_element(*Locators.Login.INPUT_EMAIL).send_keys(registered_account.email)
    webdriver.find_element(*Locators.Login.INPUT_PASSWORD).send_keys(registered_account.password)

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Login.BUTTON_LOGIN)).click()

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()

    url_before = webdriver.current_url

    if webdriver.current_url == url_before:
        wait = WebDriverWait(webdriver, TIMEOUT)
        wait.until(expected_conditions.url_changes(url_before))

    url_before = webdriver.current_url
    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'

    # Handle possible redirect from /account to account/profile
    if webdriver.current_url == url_before and not url_before == url_expected:
        wait = WebDriverWait(webdriver, TIMEOUT)
        wait.until(expected_conditions.url_changes(url_before))
