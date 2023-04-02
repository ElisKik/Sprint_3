from selenium.webdriver import Chrome as WebDriver

from locators import *
from waits import *
from javascript import *
from constants import *
from asserts import *
from utils import *
from utils import *

def test_registration(webdriver: WebDriver):
    register_account(webdriver)
    assert webdriver.current_url == f'{BASE_URL}/login'

def test_registration_short_password_failed(webdriver: WebDriver):
    go_to_base(webdriver)

    js_click(webdriver, Locators.Main.ANCHOR_ACCOUNT)
    js_click(webdriver, Locators.Account.ANCHOR_REGISTER)

    value_name = fakes.get_name()
    value_email = fakes.get_email()
    value_password = fakes.get_password()

    value_password = value_password[0:5]

    js_send_keys_focused(webdriver, Locators.Registration.INPUT_NAME, value_name)
    js_send_keys_focused(webdriver, Locators.Registration.INPUT_EMAIL, value_email)
    js_send_keys_focused(webdriver, Locators.Registration.INPUT_PASSWORD, value_password)

    js_focus(webdriver, Locators.Registration.BUTTON_REGISTER)

    assert_element_exists(
        webdriver,
        Locators.Registration.PARAGRAPH_PASSWORD_ERROR,
        'Invalid password caption was not found')

    assert webdriver.current_url == f'{BASE_URL}/register', \
           'Page changed on invalid password entered'
