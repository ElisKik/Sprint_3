"""
Common functions reusable in several tests.
"""

import time

from typing import Dict

from selenium.webdriver import Chrome as WebDriver

from locators import *
from waits import *
from javascript import *
from constants import *

from account import RegisteredAccount

import fakes

def register_account(webdriver: WebDriver) -> RegisteredAccount:
    """
    Initializes account object with random fake credentials and real name of user.

    Performs registration on target site.
    """

    name = fakes.get_name()
    email = fakes.get_email()
    password = fakes.get_password()

    account = RegisteredAccount(webdriver, name, email, password)

    return account

def go_to_base(webdriver: WebDriver):
    webdriver.get(BASE_URL)
    wait_overlay_hidden(webdriver)

def wait_overlay_hidden(webdriver: WebDriver):
    time.sleep(1)
    wait_invisible(webdriver, Locators.Main.OVERLAY)
