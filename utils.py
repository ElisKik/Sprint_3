"""
Common functions reusable in several tests.
"""

from webdriver_resolver import WebDriver

from account import RegisteredAccount
from fakes import get_name, get_email, get_password
from urls import Urls

def register_account(webdriver: WebDriver) -> RegisteredAccount:
    """
    Initializes account object with random fake credentials and real name of user.

    Performs registration on target site.
    """

    name = get_name()
    email = get_email()
    password = get_password()

    account = RegisteredAccount(webdriver, name, email, password)

    return account

def go_to_base(webdriver: WebDriver):
    """
    Opens home page of target site.
    """

    webdriver.get(Urls.BASE)
