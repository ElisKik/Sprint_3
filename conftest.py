"""
Script for definitions of fixtures.
"""

import pytest

from typing import Iterable

from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.chrome.options import Options

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
