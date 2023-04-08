"""
Shortcuts for using :class:`selenium.webdriver.support.expected_conditions`
"""

from typing import List

from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.remote.webelement import WebElement
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

    wait = WebDriverWait(webdriver, TIMEOUT, WAIT_POLL_FREQUENCY)
    wait.until(expected_conditions.presence_of_element_located(locator)).click()

def wait_page_loaded(webdriver: WebDriver, current_url: str) -> None:
    """
    Waits for current URL of driver being changed
    in comparison to `current_url` given as an argument.
    """

    if webdriver.current_url == current_url:
        wait = WebDriverWait(webdriver, TIMEOUT, WAIT_POLL_FREQUENCY)
        wait.until(expected_conditions.url_changes(current_url))

def wait_visible(webdriver: WebDriver, locator: Locator) -> bool:
    """
    Performs `visibility_of_element_located()`
    via :class:`expected_conditions` and returns the result.
    """

    wait = WebDriverWait(webdriver, TIMEOUT, WAIT_POLL_FREQUENCY)
    is_visible = wait.until(expected_conditions.visibility_of_element_located(locator))

    return is_visible

def wait_find_elements(webdriver: WebDriver, locator: Locator) -> List[WebElement]:
    """
    Performs `presence_of_all_elements_located()`
    via :class:`expected_conditions` and returns the result.
    """

    wait = WebDriverWait(webdriver, TIMEOUT, WAIT_POLL_FREQUENCY)
    elements = wait.until(expected_conditions.presence_of_all_elements_located(locator))

    return elements
