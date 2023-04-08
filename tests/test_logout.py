from selenium.webdriver import Chrome as WebDriver

from asserts import assert_login
from locators import Locators
from urls import Urls
from utils import register_account
from waits import wait_obscured_click, wait_page_loaded

def test_logout(webdriver: WebDriver):
    registered_account = register_account(webdriver)

    assert_login(webdriver, registered_account)

    url_before = webdriver.current_url

    wait_obscured_click(webdriver, Locators.Profile.BUTTON_LOGOUT)

    if webdriver.current_url == url_before:
        wait_page_loaded(webdriver, url_before)

    assert webdriver.current_url == f'{Urls.BASE}/{Urls.LOGIN}'
