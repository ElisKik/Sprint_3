"""
Wrapper functions that perform JavaScript calls on DOM elements
found with given locators.
"""

from os import path

from webdriver_resolver import WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from aliases import Locator
from constants import TIMEOUT

def __load_js_function(script_relative_path: str) -> str:
    """
    Loads JavaScript function from file
    at given relative path.
    """

    script_full_path = path.realpath(
        path.join(
            path.dirname(__file__),
            script_relative_path))

    with open(script_full_path, 'r') as script_file:
        return script_file.read()

__js_functions = {
    'isScrolledIntoView': __load_js_function('js/is-scrolled-into-view.js')
}
"""
Cache of JavaScript functions loaded from files.
"""

def __get_js_function_call(function_name: str, returns: bool = False) -> str:
    """
    Formats call of requested JavaScript function
    loaded from file.

    Returning of value also can be included
    in the result string.
    """

    source = __js_functions[function_name]

    source += '\n'

    if returns:
        source += "return "

    source += f'{function_name}(arguments[0])'

    return source

def js_focus(webdriver: WebDriver, locator: Locator) -> None:
    """
    Waits for an element at given locator to be present
    and performs `focus()` using JavaScript.
    """

    wait = WebDriverWait(webdriver, TIMEOUT)
    element = wait.until(expected_conditions.presence_of_element_located(locator))
    webdriver.execute_script('arguments[0].focus();', element)

def js_click(webdriver: WebDriver, locator: Locator) -> None:
    """
    Waits for an element at given locator to be present
    and performs `click()` using JavaScript.
    """

    wait = WebDriverWait(webdriver, TIMEOUT)
    element = wait.until(expected_conditions.presence_of_element_located(locator))
    webdriver.execute_script('arguments[0].click();', element)

def js_wait_scrolled_into_view(webdriver: WebDriver, locator: Locator) -> None:
    """
    Waits for an element at given locator to be present
    and then waits for an element being scrolled into
    visible rect of screen.
    """

    wait = WebDriverWait(webdriver, TIMEOUT)
    element = wait.until(expected_conditions.presence_of_element_located(locator))

    js_function_call = __get_js_function_call('isScrolledIntoView', returns=True)

    wait = WebDriverWait(webdriver, TIMEOUT)
    wait.until(lambda driver: driver.execute_script(js_function_call, element))

def js_check_scrolled_into_view(webdriver: WebDriver, locator: Locator) -> bool:
    """
    Waits for an element at given locator to be present
    and then checks for an element being scrolled into
    visible rect of screen.
    """

    wait = WebDriverWait(webdriver, TIMEOUT)
    element = wait.until(expected_conditions.presence_of_element_located(locator))

    js_function_call = __get_js_function_call('isScrolledIntoView', returns=True)

    return webdriver.execute_script(js_function_call, element)
