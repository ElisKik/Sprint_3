from selenium.webdriver import Chrome as WebDriver

from asserts import assert_login
from locators import Locators
from urls import Urls
from utils import register_account
from waits import wait_click, wait_obscured_click

def test_login_main(webdriver: WebDriver):
    registered_account = register_account(webdriver)
    webdriver.get(Urls.BASE)
    wait_obscured_click(webdriver, Locators.Main.BUTTON_LOGIN)
    assert_login(webdriver, registered_account)

def test_login_account(webdriver: WebDriver):
    registered_account = register_account(webdriver)
    webdriver.get(Urls.BASE)
    wait_obscured_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
    assert_login(webdriver, registered_account)

def test_login_registration(webdriver: WebDriver):
    registered_account = register_account(webdriver)
    assert_login(webdriver, registered_account)

def test_login_password_recovery(webdriver: WebDriver):
    webdriver.get(Urls.BASE)

    wait_obscured_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
    wait_click(webdriver, Locators.Account.ANCHOR_RECOVER_PASSWORD)
    wait_click(webdriver, Locators.PasswordRecovery.ANCHOR_LOGIN)

    assert webdriver.current_url == f'{Urls.BASE}/{Urls.LOGIN}'
