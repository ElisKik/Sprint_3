from selenium.webdriver import Chrome as WebDriver

from account import RegisteredAccount
from asserts import assert_login

def test_go_to_account(webdriver: WebDriver, registered_account: RegisteredAccount):
    assert_login(webdriver, registered_account)
