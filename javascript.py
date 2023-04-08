"""
Wrapper functions that perform JavaScript calls on DOM elements
found with given locators.
"""

from selenium.webdriver import Chrome as WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from aliases import Locator
from constants import TIMEOUT

"""
Cache of JavaScript functions loaded from files.
"""

def js_click(webdriver: WebDriver, locator: Locator) -> None:
    """
    Waits for an element at given locator to be present
    and performs `click()` using JavaScript.
    """

    wait = WebDriverWait(webdriver, TIMEOUT)
    element = wait.until(expected_conditions.presence_of_element_located(locator))
    webdriver.execute_script('arguments[0].click();', element)
