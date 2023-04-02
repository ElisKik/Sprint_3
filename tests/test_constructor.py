# -*- coding: utf8 -*-

import pytest

from selenium.webdriver import Chrome as WebDriver

from locators import *
from waits import *
from javascript import *
from constants import *
from asserts import *
from utils import *

def test_go_to_constructor_from_logo(webdriver: WebDriver):
    go_to_base(webdriver)

    js_click(webdriver, Locators.Main.ANCHOR_LOGO)

    assert_element_exists(
        webdriver,
        Locators.Constructor.CONTAINER_INGREDIENTS,
        'Ingredients container was not found')

def test_go_to_constructor_from_header(webdriver: WebDriver):
    go_to_base(webdriver)

    js_click(webdriver, Locators.Header.ANCHOR_CONSTRUCTOR)

    assert_element_exists(
        webdriver,
        Locators.Constructor.CONTAINER_INGREDIENTS,
        'Ingredients container was not found')

@pytest.mark.parametrize(
    'ingredient_group',
    [
        u'Булки',
        u'Соусы',
        u'Начинки',
    ],
    ids=[
        'buns',
        'sauces',
        'toppings',
    ])
def test_go_to_ingredient_group(webdriver: WebDriver, ingredient_group):
    go_to_base(webdriver)

    js_click(webdriver, Locators.Header.ANCHOR_CONSTRUCTOR)

    js_click(
        webdriver,
        Locators.Constructor.get_span_ingredient_group(ingredient_group))

    time.sleep(1)

    assert js_check_scrolled_into_view(
        webdriver,
        Locators.Constructor.get_title_ingredient_group(ingredient_group))
