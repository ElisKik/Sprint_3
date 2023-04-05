"""
Imports driver for a browser specified via environment variable.

Valid values:
- ```SELENIUM_DRIVER=chrome``` (default)
- ```SELENIUM_DRIVER=firefox```

Usage:\n
Prepend call of `pytest` with specifying environment variable
only for current process:
```bash
SELENIUM_DRIVER=firefox pytest -v tests
```
"""

from os import environ

driver = environ.get('SELENIUM_DRIVER', 'chrome')

if driver == 'chrome':
    from selenium.webdriver import Chrome as WebDriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager as DriverManager
elif driver == 'firefox':
    from selenium.webdriver import Firefox as WebDriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager as DriverManager
else:
    raise Exception(f'Driver {driver} is not supported by these tests')
