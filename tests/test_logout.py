from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import TIMEOUT
from locators import Locators
from urls import Urls
from utils import login, register_account

def test_logout(webdriver: WebDriver):
    registered_account = register_account(webdriver)

    webdriver.get(Urls.BASE)

    login(webdriver, registered_account)

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Profile.PARAGRAPH_DESCRIPTION))

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Profile.BUTTON_LOGOUT)).click()

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Account.ANCHOR_RECOVER_PASSWORD))

    url_expected = f'{Urls.BASE}/{Urls.LOGIN}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, 'Logout has failed'
