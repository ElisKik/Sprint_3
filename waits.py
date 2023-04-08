"""
Shortcuts for using :class:`selenium.webdriver.support.expected_conditions`
"""

from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.remote.errorhandler import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from aliases import Locator
from constants import TIMEOUT, WAIT_POLL_FREQUENCY

def wait_click(webdriver: WebDriver, locator: Locator) -> None:
    """
    Performs `presence_of_element_located()`
    via :class:`expected_conditions`
    and then `click()` via WebDriver.
    """

    wait = __wait_factory(webdriver)
    element = wait.until(expected_conditions.presence_of_element_located(locator))
    element.click()

def wait_obscured_click(webdriver: WebDriver, locator: Locator) -> None:
    """
    Performs attempts to `click()` via WebDriver,
    ignoring :class:`ElementClickInterceptedException`
    """

    wait = __wait_factory(webdriver)
    wait.until(lambda driver: __try_click(driver, locator))

def wait_page_loaded(webdriver: WebDriver, current_url: str) -> None:
    """
    Waits for an element at given locator to be present
    and then waits for current URL of driver being changed
    in comparison to `current_url` given as an argument.
    """

    wait = __wait_factory(webdriver)
    wait.until(expected_conditions.url_changes(current_url))

def wait_send_keys(webdriver: WebDriver, locator: Locator, keys: str):
    """
    Waits for an element at given locator to be present
    and performs `send_keys()` via WebDriver.
    """

    wait = WebDriverWait(webdriver, TIMEOUT)
    element = wait.until(expected_conditions.element_to_be_clickable(locator))

    element.send_keys(keys)

def __wait_factory(webdriver: WebDriver) -> WebDriverWait:
    """
    Creates instance of :class:`WebDriverWait` with
    constants `TIMEOUT` and `WAIT_POLL_FREQUENCY`
    specified in this project.
    """
    return WebDriverWait(webdriver, TIMEOUT, WAIT_POLL_FREQUENCY)

def __try_click(webdriver: WebDriver, locator: Locator) -> bool:
    element = webdriver.find_element(*locator)

    try:
        element.click()
        return True
    except ElementClickInterceptedException:
        return False
