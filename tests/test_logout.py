from selenium.webdriver import Chrome as WebDriver

from locators import Locators
from urls import Urls
from utils import login, register_account
from waits import wait_click, wait_page_loaded

def test_logout(webdriver: WebDriver):
    registered_account = register_account(webdriver)

    login(webdriver, registered_account)

    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, \
           f'Login with registered account has failed, URL\
            \nexpected: {url_expected},\
            \nactual: {url_actual}'

    url_before = webdriver.current_url

    wait_click(webdriver, Locators.Profile.BUTTON_LOGOUT)

    wait_page_loaded(webdriver, url_before)

    url_expected = f'{Urls.BASE}/{Urls.LOGIN}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, \
           f'Logout has failed, URL\
            \nexpected: {url_expected},\
            \nactual: {url_actual}'
