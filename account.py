import time

from selenium.webdriver import Chrome as WebDriver

from locators import *
from waits import *
from javascript import *

class RegisteredAccount:
    """
    Initializes account object with given credentials and real name of user.

    Performs registration on target site at initialization.
    """

    def __init__(self, webdriver: WebDriver, name: str, email: str, password: str):
        webdriver.get(BASE_URL)

        time.sleep(1)
        wait_invisible(webdriver, Locators.Main.OVERLAY)

        js_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
        js_click(webdriver, Locators.Account.ANCHOR_REGISTER)

        self.name = name
        self.email = email
        self.password = password

        js_send_keys_focused(webdriver, Locators.Registration.INPUT_NAME, self.name)
        js_send_keys_focused(webdriver, Locators.Registration.INPUT_EMAIL, self.email)
        js_send_keys_focused(webdriver, Locators.Registration.INPUT_PASSWORD, self.password)

        js_click(webdriver, Locators.Registration.BUTTON_REGISTER)

        time.sleep(1)
        wait_invisible(webdriver, Locators.Main.OVERLAY)

