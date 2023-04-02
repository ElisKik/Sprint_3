"""
Functions that encapsulate generation of random fake data.

Current implementation: via :class:`fake.Faker`
"""

from faker import Faker

faker = Faker('ru_RU')

def get_email() -> str:
    return faker.email()

def get_name() -> str:
    faker = Faker('ru_RU')
    return faker.name()

def get_password() -> str:
    faker = Faker()
    return faker.password()
