from selenium.webdriver import Chrome as WebDriver

from locators import *
from waits import *
from javascript import *
from constants import *
from asserts import *
from utils import *

from account import RegisteredAccount

def test_login_main(webdriver: WebDriver, registered_account: RegisteredAccount):
    go_to_base(webdriver)
    js_click(webdriver, Locators.Main.BUTTON_LOGIN)
    assert_login(webdriver, registered_account)

def test_login_account(webdriver: WebDriver, registered_account: RegisteredAccount):
    go_to_base(webdriver)
    js_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
    assert_login(webdriver, registered_account)

def test_login_registration(webdriver: WebDriver, registered_account: RegisteredAccount):
    assert_login(webdriver, registered_account)

def test_login_password_recovery(webdriver: WebDriver):
    go_to_base(webdriver)

    js_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
    js_click(webdriver, Locators.Account.ANCHOR_RECOVER_PASSWORD)
    js_click(webdriver, Locators.PasswordRecovery.ANCHOR_LOGIN)

    assert webdriver.current_url == f'{BASE_URL}/login'
