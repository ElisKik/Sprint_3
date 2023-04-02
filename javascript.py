"""
Wrapper functions that perform JavaScript calls on DOM elements
found with given locators.
"""

from os import path

from selenium.webdriver import Chrome as WebDriver

from aliases import Locator

def __load_js_function(script_relative_path: str):
    script_full_path = path.realpath(
        path.join(
            path.dirname(__file__),
            script_relative_path))

    with open(script_full_path, 'r') as script_file:
        return script_file.read()

__js_functions = {
    'isScrolledIntoView': __load_js_function('js/is-scrolled-into-view.js')
}

def __get_js_function_call(function_name: str, returns: bool = False):
    source = __js_functions[function_name]

    source += '\n'

    if returns:
        source += "return "

    source += f'{function_name}(arguments[0])'

    return source

def js_focus(webdriver: WebDriver, locator: Locator) -> None:
    element = webdriver.find_element(*locator)
    webdriver.execute_script('arguments[0].focus();', element)

def js_click(webdriver: WebDriver, locator: Locator) -> None:
    element = webdriver.find_element(*locator)
    webdriver.execute_script('arguments[0].click();', element)

def js_click_focused(webdriver: WebDriver, locator: Locator) -> None:
    element = webdriver.find_element(*locator)
    webdriver.execute_script('arguments[0].focus();', element)

    element = webdriver.find_element(*locator)
    webdriver.execute_script('arguments[0].click();', element)

def js_send_keys_focused(webdriver: WebDriver, locator: Locator, keys: str) -> None:
    element = webdriver.find_element(*locator)
    webdriver.execute_script('arguments[0].focus();', element)

    element = webdriver.find_element(*locator)
    element.send_keys(keys)

def js_check_scrolled_into_view(webdriver: WebDriver, locator: Locator) -> bool:
    element = webdriver.find_element(*locator)
    js_function_call = __get_js_function_call('isScrolledIntoView', returns=True)
    return webdriver.execute_script(js_function_call, element)
