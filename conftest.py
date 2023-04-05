"""
Script for definitions of fixtures.
"""

import pytest

from os import environ
from typing import Iterable

from webdriver_resolver import DriverManager, WebDriver, Options, Service

from account import RegisteredAccount
from utils import register_account

@pytest.fixture()
def webdriver() -> Iterable[WebDriver]:
    """
    Fixture of Selenium WebDriver configured
    with maximized window and headless mode
    by default.
    """

    is_headless = bool(int(environ.get('SELENIUM_HEADLESS', '1')))
    is_maximized = bool(int(environ.get('SELENIUM_MAXIMIZED', '1')))

    options = Options()

    if is_headless:
        options.add_argument('--headless')

    driverManager = DriverManager().install()
    webdriver = WebDriver(service=Service(driverManager), options=options)

    if is_maximized:
        webdriver.maximize_window()

    yield webdriver

    webdriver.quit()

@pytest.fixture()
def registered_account(webdriver: WebDriver) -> RegisteredAccount:
    """
    Fixture which performs registration of a new account.
    """

    return register_account(webdriver)
