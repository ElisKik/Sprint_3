from selenium.webdriver import Chrome as WebDriver

from constants import PASSWORD_LENGTH_MIN
from fakes import get_name, get_email, get_password
from locators import Locators
from urls import Urls
from utils import register_account
from waits import wait_find_elements, wait_page_loaded

def test_registration(webdriver: WebDriver):
    url_before = webdriver.current_url
    register_account(webdriver)

    wait_page_loaded(webdriver, url_before)

    assert webdriver.current_url == f'{Urls.BASE}/{Urls.LOGIN}'

def test_registration_short_password_failed(webdriver: WebDriver):
    webdriver.get(Urls.BASE)

    webdriver.find_element(*Locators.Main.ANCHOR_ACCOUNT).click()
    webdriver.find_element(*Locators.Account.ANCHOR_REGISTER).click()

    value_name = get_name()
    value_email = get_email()
    value_password = get_password()

    invalid_password_length = PASSWORD_LENGTH_MIN - 1

    value_password = value_password[0:invalid_password_length]

    webdriver.find_element(*Locators.Registration.INPUT_NAME).send_keys(value_name)
    webdriver.find_element(*Locators.Registration.INPUT_EMAIL).send_keys(value_email)
    webdriver.find_element(*Locators.Registration.INPUT_PASSWORD).send_keys(value_password)

    webdriver.find_element(*Locators.Registration.BUTTON_REGISTER).click()

    found_elements = wait_find_elements(webdriver, Locators.Registration.PARAGRAPH_PASSWORD_ERROR)

    assert len(found_elements) > 0, 'Invalid password caption was not found'
    assert len(found_elements) == 1, 'Ambiguous results of searching for invalid password caption'

    assert webdriver.current_url == f'{Urls.BASE}/{Urls.REGISTER}', \
           'Page changed on invalid password entered'
