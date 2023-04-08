from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fakes import get_name, get_email, get_password
from locators import Locators

class RegisteredAccount:
    """
    Object for storing credentials and real name of user.
    """

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

class Account:
    """
    Provides functions for registration and login of account.
    """

    def __init__(self, webdriver: WebDriver, wait: WebDriverWait):
        self.webdriver = webdriver
        self.wait = wait

    def register(self) -> RegisteredAccount:
        """
        Returns object with random fake credentials and real name of user.

        Performs registration on target site.
        """

        self.webdriver.find_element(*Locators.Main.ANCHOR_ACCOUNT).click()
        self.webdriver.find_element(*Locators.Account.ANCHOR_REGISTER).click()

        name = get_name()
        email = get_email()
        password = get_password()

        self.webdriver.find_element(*Locators.Registration.INPUT_NAME).send_keys(name)
        self.webdriver.find_element(*Locators.Registration.INPUT_EMAIL).send_keys(email)
        self.webdriver.find_element(*Locators.Registration.INPUT_PASSWORD).send_keys(password)

        self.webdriver.find_element(*Locators.Registration.BUTTON_REGISTER).click()

        return RegisteredAccount(name, email, password)

    def login(self, registered_account: RegisteredAccount) -> None:
        """
        Performs login with given object of registered account.
        """

        self.wait.until(expected_conditions.presence_of_element_located(Locators.Main.BUTTON_LOGIN)).click()

        self.wait.until(expected_conditions.presence_of_element_located(Locators.Login.INPUT_EMAIL)).send_keys(registered_account.email)

        self.webdriver.find_element(*Locators.Login.INPUT_PASSWORD).send_keys(registered_account.password)

        form_login_element = self.webdriver.find_element(*Locators.Login.FORM_LOGIN)

        self.wait.until(expected_conditions.presence_of_element_located(Locators.Login.BUTTON_LOGIN)).click()
        self.wait.until(expected_conditions.staleness_of(form_login_element))
