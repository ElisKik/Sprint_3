from selenium.webdriver import Chrome as WebDriver

from asserts import assert_login
from utils import register_account

def test_go_to_account(webdriver: WebDriver):
    registered_account = register_account(webdriver)
    assert_login(webdriver, registered_account)
