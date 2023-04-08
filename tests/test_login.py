from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from account import Account
from fakes import get_name, get_email, get_password
from locators import Locators
from urls import Urls

class TestLogin:
    @staticmethod
    def test_login_main(webdriver: WebDriver, wait: WebDriverWait):
        wait.until(expected_conditions.presence_of_element_located(Locators.Main.BUTTON_LOGIN)).click()

        wait.until(expected_conditions.presence_of_element_located(Locators.Account.ANCHOR_REGISTER)).click()

        name = get_name()
        email = get_email()
        password = get_password()

        wait.until(expected_conditions.presence_of_element_located(Locators.Registration.INPUT_NAME)).send_keys(name)

        webdriver.find_element(*Locators.Registration.INPUT_EMAIL).send_keys(email)
        webdriver.find_element(*Locators.Registration.INPUT_PASSWORD).send_keys(password)

        webdriver.find_element(*Locators.Registration.BUTTON_REGISTER).click()

        wait.until(expected_conditions.presence_of_element_located(Locators.Account.ANCHOR_RECOVER_PASSWORD))

        wait.until(expected_conditions.presence_of_element_located(Locators.Login.INPUT_EMAIL)).send_keys(email)
        wait.until(expected_conditions.presence_of_element_located(Locators.Login.INPUT_PASSWORD)).send_keys(password)

        form_login_element = webdriver.find_element(*Locators.Login.FORM_LOGIN)

        wait.until(expected_conditions.presence_of_element_located(Locators.Login.BUTTON_LOGIN)).click()
        wait.until(expected_conditions.staleness_of(form_login_element))

        wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()
        wait.until(expected_conditions.presence_of_element_located(Locators.Profile.PARAGRAPH_DESCRIPTION))

        url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
        url_actual = webdriver.current_url

        assert url_actual == url_expected, 'Login with registered account has failed'

    @staticmethod
    def test_login_account(webdriver: WebDriver, account: Account, wait: WebDriverWait):
        registered_account = account.register()

        webdriver.get(Urls.BASE)

        account.login(registered_account)

        wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()

        wait.until(expected_conditions.presence_of_element_located(Locators.Profile.PARAGRAPH_DESCRIPTION))

        url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
        url_actual = webdriver.current_url

        assert url_actual == url_expected, 'Login with registered account has failed'

    @staticmethod
    def test_login_registration(webdriver: WebDriver, account: Account, wait: WebDriverWait):
        registered_account = account.register()

        webdriver.get(Urls.BASE)

        account.login(registered_account)

        wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()

        wait.until(expected_conditions.presence_of_element_located(Locators.Profile.PARAGRAPH_DESCRIPTION))

        url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
        url_actual = webdriver.current_url

        assert url_actual == url_expected, 'Login with registered account has failed'

    @staticmethod
    def test_login_password_recovery(webdriver: WebDriver, wait: WebDriverWait):
        wait.until(expected_conditions.presence_of_element_located(Locators.Main.ANCHOR_ACCOUNT)).click()
        wait.until(expected_conditions.presence_of_element_located(Locators.Account.ANCHOR_RECOVER_PASSWORD)).click()
        wait.until(expected_conditions.presence_of_element_located(Locators.PasswordRecovery.ANCHOR_LOGIN)).click()

        url_expected = f'{Urls.BASE}/{Urls.LOGIN}'
        url_actual = webdriver.current_url

        assert url_actual == url_expected, 'Login from password recovery page has failed'
