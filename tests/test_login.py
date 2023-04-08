from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import TIMEOUT
from locators import Locators
from urls import Urls
from utils import register_account, login

def test_login_main(webdriver: WebDriver):
    registered_account = register_account(webdriver)

    webdriver.get(Urls.BASE)

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Main.BUTTON_LOGIN)).click()

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

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()

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

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Account.ANCHOR_RECOVER_PASSWORD)).click()

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.PasswordRecovery.ANCHOR_LOGIN)).click()

    url_expected = f'{Urls.BASE}/{Urls.LOGIN}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, \
           f'Login from password recovery page has failed, URL\
            \nexpected: {url_expected},\
            \nactual: {url_actual}'
