from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from account import Account
from constants import TIMEOUT
from locators import Locators
from urls import Urls

def test_go_to_account(webdriver: WebDriver, account: Account):
    registered_account = account.register()

    webdriver.get(Urls.BASE)

    account.login(registered_account)

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.presence_of_element_located(Locators.Profile.PARAGRAPH_DESCRIPTION))

    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, 'Login with registered account has failed'
