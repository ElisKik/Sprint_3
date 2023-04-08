from selenium.webdriver import Chrome as WebDriver

from locators import Locators
from urls import Urls
from utils import register_account, login
from waits import wait_click, wait_obscured_click

def test_login_main(webdriver: WebDriver):
    registered_account = register_account(webdriver)

    webdriver.get(Urls.BASE)

    wait_obscured_click(webdriver, Locators.Main.BUTTON_LOGIN)

    login(webdriver, registered_account)

    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, \
           f'Login with registered account has failed, URL\
            \nexpected: {url_expected},\
            \nactual: {url_actual}'

def test_login_account(webdriver: WebDriver):
    registered_account = register_account(webdriver)

    webdriver.get(Urls.BASE)

    wait_obscured_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)

    login(webdriver, registered_account)

    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, \
           f'Login with registered account has failed, URL\
            \nexpected: {url_expected},\
            \nactual: {url_actual}'

def test_login_registration(webdriver: WebDriver):
    registered_account = register_account(webdriver)

    login(webdriver, registered_account)

    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, \
           f'Login with registered account has failed, URL\
            \nexpected: {url_expected},\
            \nactual: {url_actual}'

def test_login_password_recovery(webdriver: WebDriver):
    webdriver.get(Urls.BASE)

    wait_obscured_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
    wait_click(webdriver, Locators.Account.ANCHOR_RECOVER_PASSWORD)
    wait_click(webdriver, Locators.PasswordRecovery.ANCHOR_LOGIN)

    assert webdriver.current_url == f'{Urls.BASE}/{Urls.LOGIN}'
