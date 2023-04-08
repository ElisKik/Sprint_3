from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import TIMEOUT, PASSWORD_LENGTH_MIN
from fakes import get_name, get_email, get_password
from locators import Locators
from urls import Urls
from utils import register_account

def test_registration(webdriver: WebDriver):
    url_before = webdriver.current_url
    register_account(webdriver)

    if webdriver.current_url == url_before:
        wait = WebDriverWait(webdriver, TIMEOUT)
        wait.until(expected_conditions.url_changes(url_before))

    url_expected = f'{Urls.BASE}/{Urls.LOGIN}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, \
           f'Registration has failed, URL\
            \nexpected: {url_expected},\
            \nactual: {url_actual}'

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

    wait = WebDriverWait(webdriver, TIMEOUT)

    found_elements = wait.until(
        expected_conditions.presence_of_all_elements_located(
            Locators.Registration.PARAGRAPH_PASSWORD_ERROR))

    assert len(found_elements) > 0, 'Invalid password caption was not found'
    assert len(found_elements) == 1, 'Ambiguous results of searching for invalid password caption'

    assert webdriver.current_url == f'{Urls.BASE}/{Urls.REGISTER}', \
           'Page changed on invalid password entered'
