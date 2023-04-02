class Scope:
    """
    Constants that represent scope literals
    accepted by `pytest.fixture(scope=)`
    """

    FUNCTION = 'function'
    CLASS = 'class'
    MODULE = 'module'
    PACKAGE = 'package'
    SESSION = 'session'
