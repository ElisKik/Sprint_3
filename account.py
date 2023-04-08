from selenium.webdriver import Chrome as WebDriver

from javascript import js_click
from locators import Locators
from urls import Urls
from waits import wait_page_loaded, wait_send_keys

class RegisteredAccount:
    """
    Initializes account object with given credentials and real name of user.

    Performs registration on target site at initialization.
    """

    def __init__(self, webdriver: WebDriver, name: str, email: str, password: str):
        webdriver.get(Urls.BASE)

        js_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
        js_click(webdriver, Locators.Account.ANCHOR_REGISTER)

        self.name = name
        self.email = email
        self.password = password

        wait_send_keys(webdriver, Locators.Registration.INPUT_NAME, self.name)
        wait_send_keys(webdriver, Locators.Registration.INPUT_EMAIL, self.email)
        wait_send_keys(webdriver, Locators.Registration.INPUT_PASSWORD, self.password)

        url_before = webdriver.current_url

        js_click(webdriver, Locators.Registration.BUTTON_REGISTER)

        if webdriver.current_url == url_before:
            wait_page_loaded(webdriver, url_before)

