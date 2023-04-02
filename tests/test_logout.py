from selenium.webdriver import Chrome as WebDriver

from locators import *
from waits import *
from javascript import *
from constants import *
from asserts import *
from utils import *

from account import RegisteredAccount

def test_logout(webdriver: WebDriver, registered_account: RegisteredAccount):
    assert_login(webdriver, registered_account)
    js_click(webdriver, Locators.Profile.BUTTON_LOGOUT)
    wait_overlay_hidden(webdriver)
    assert webdriver.current_url == f'{BASE_URL}/login'
