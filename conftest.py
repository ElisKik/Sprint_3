"""
Script for definitions of fixtures.
"""

import pytest

from typing import Iterable

from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.chrome.options import Options

from account import RegisteredAccount
from utils import register_account

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

    yield webdriver

    webdriver.quit()

@pytest.fixture()
def registered_account(webdriver: WebDriver) -> RegisteredAccount:
    """
    Fixture which performs registration of a new account.
    """

    return register_account(webdriver)
