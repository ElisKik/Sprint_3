import pytest

from typing import Iterable

from webdriver_manager.chrome import ChromeDriverManager as DriverManager

from selenium.webdriver import Chrome as WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from scope import Scope
from account import RegisteredAccount

from constants import *
from utils import *

@pytest.fixture(scope=Scope.FUNCTION)
def webdriver() -> Iterable[WebDriver]:
    options = Options()
    options.add_argument('--headless')

    driverManager = DriverManager().install()
    webdriver = WebDriver(service=Service(driverManager), options=options)

    webdriver.maximize_window()

    yield webdriver

    webdriver.quit()

@pytest.fixture(scope=Scope.FUNCTION)
def registered_account(webdriver: WebDriver) -> RegisteredAccount:
    return register_account(webdriver)
