"""
Functions that encapsulate generation of random fake data.

Current implementation: via :class:`fake.Faker`
"""

from faker import Faker

from constants import PASSWORD_LENGTH_MIN

faker_common = Faker('ru_RU')
faker_passwords = Faker()

def get_email() -> str:
    """
    Gets a random email address
    with `ru_RU` locale.

    Using :class:`fake.Faker`
    """

    return faker_common.email()

def get_name() -> str:
    """
    Gets a random real name of user
    with `ru_RU` locale.

    Using :class:`fake.Faker`
    """

    return faker_common.name()

def get_password() -> str:
    """
    Gets a random real name for the user
    with unspecified locale.

    Using :class:`fake.Faker`
    """

    return faker_passwords.password(length=PASSWORD_LENGTH_MIN)
