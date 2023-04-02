from selenium.webdriver import Chrome as WebDriver

from locators import *
from waits import *
from javascript import *
from constants import *
from asserts import *
from utils import *

from account import RegisteredAccount

def test_go_to_account(webdriver: WebDriver, registered_account: RegisteredAccount):
    assert_login(webdriver, registered_account)
