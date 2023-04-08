"""
Shortcuts for using :class:`selenium.webdriver.support.expected_conditions`
"""

from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import TIMEOUT, WAIT_POLL_FREQUENCY

def wait_page_loaded(webdriver: WebDriver, current_url: str) -> None:
    """
    Waits for current URL of driver being changed
    in comparison to `current_url` given as an argument.
    """

    if webdriver.current_url == current_url:
        wait = WebDriverWait(webdriver, TIMEOUT, WAIT_POLL_FREQUENCY)
        wait.until(expected_conditions.url_changes(current_url))
