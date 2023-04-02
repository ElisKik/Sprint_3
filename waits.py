"""
Shortcuts for using :class:`selenium.webdriver.support.expected_conditions`
"""

from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from aliases import Locator

from constants import *

def wait_present(webdriver: WebDriver, locator: Locator) -> WebElement:
    wait = WebDriverWait(webdriver, TIMEOUT)
    return wait.until(expected_conditions.presence_of_element_located(locator))

def wait_visible(webdriver: WebDriver, locator: Locator) -> WebElement:
    wait = WebDriverWait(webdriver, TIMEOUT)
    return wait.until(expected_conditions.visibility_of_element_located(locator))

def wait_clickable(webdriver: WebDriver, locator: Locator) -> WebElement:
    wait = WebDriverWait(webdriver, TIMEOUT)
    return wait.until(expected_conditions.element_to_be_clickable(locator))

def wait_invisible(webdriver: WebDriver, locator: Locator) -> None:
    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(expected_conditions.invisibility_of_element(locator))
