from selenium.webdriver import Chrome as WebDriver

from constants import PASSWORD_LENGTH_MIN
from fakes import get_name, get_email, get_password
from javascript import js_click, js_focus
from locators import Locators
from urls import Urls
from utils import register_account
from waits import wait_page_loaded, wait_send_keys

def test_registration(webdriver: WebDriver):
    url_before = webdriver.current_url
    register_account(webdriver)

    wait_page_loaded(webdriver, url_before)

    assert webdriver.current_url == f'{Urls.BASE}/{Urls.LOGIN}'

def test_registration_short_password_failed(webdriver: WebDriver):
    webdriver.get(Urls.BASE)

    js_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
    js_click(webdriver, Locators.Account.ANCHOR_REGISTER)

    value_name = get_name()
    value_email = get_email()
    value_password = get_password()

    invalid_password_length = PASSWORD_LENGTH_MIN - 1

    value_password = value_password[0:invalid_password_length]

    wait_send_keys(webdriver, Locators.Registration.INPUT_NAME, value_name)
    wait_send_keys(webdriver, Locators.Registration.INPUT_EMAIL, value_email)
    wait_send_keys(webdriver, Locators.Registration.INPUT_PASSWORD, value_password)

    js_focus(webdriver, Locators.Registration.BUTTON_REGISTER)

    found_elements = webdriver.find_elements(*Locators.Registration.PARAGRAPH_PASSWORD_ERROR)

    assert len(found_elements) > 0, 'Invalid password caption was not found'
    assert len(found_elements) == 1, 'Ambiguous results of searching for invalid password caption'

    assert webdriver.current_url == f'{Urls.BASE}/{Urls.REGISTER}', \
           'Page changed on invalid password entered'
