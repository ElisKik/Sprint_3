"""
Script for definitions of fixtures.
"""

import pytest

from typing import Iterable

from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from account import Account
from constants import TIMEOUT
from urls import Urls

@pytest.fixture()
def webdriver() -> Iterable[WebDriver]:
    """
    Fixture of Selenium WebDriver configured
    with maximized window and headless mode
    by default.
    """
    options = Options()

    options.add_argument('--headless')

    webdriver = WebDriver(options=options)

    webdriver.maximize_window()

    webdriver.get(Urls.BASE)

    yield webdriver

    webdriver.quit()

@pytest.fixture()
def wait(webdriver: WebDriver) -> WebDriverWait:
    """
    Fixture that returns instance of :class:`WebDriverWait`
    """

    return WebDriverWait(webdriver, TIMEOUT)

@pytest.fixture()
def account(webdriver: WebDriver, wait: WebDriverWait) -> Account:
    """
    Fixture that returns object which providing
    functions for account at Stellar Burgers.
    """

    return Account(webdriver, wait)
