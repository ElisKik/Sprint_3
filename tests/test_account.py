from selenium.webdriver import Chrome as WebDriver

from utils import register_account
from urls import Urls
from utils import login

def test_go_to_account(webdriver: WebDriver):
    registered_account = register_account(webdriver)

    login(webdriver, registered_account)

    url_expected = f'{Urls.BASE}/{Urls.PROFILE}'
    url_actual = webdriver.current_url

    assert url_actual == url_expected, \
           f'Login with registered account has failed, URL\
            \nexpected: {url_expected},\
            \nactual: {url_actual}'
