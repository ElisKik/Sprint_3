# -*- coding: utf8 -*-

import pytest

from selenium.webdriver import Chrome as WebDriver

from javascript import js_click, js_check_scrolled_into_view, js_wait_scrolled_into_view
from locators import Locators
from urls import Urls

def test_go_to_constructor_from_logo(webdriver: WebDriver):
    webdriver.get(Urls.BASE)

    js_click(webdriver, Locators.Main.ANCHOR_LOGO)

    found_elements = webdriver.find_elements(*Locators.Constructor.CONTAINER_INGREDIENTS)

    assert len(found_elements) > 0, 'Ingredients container was not found'
    assert len(found_elements) == 1, 'Ambiguous results of searching for ingredients container'

def test_go_to_constructor_from_header(webdriver: WebDriver):
    webdriver.get(Urls.BASE)

    js_click(webdriver, Locators.Header.ANCHOR_CONSTRUCTOR)

    found_elements = webdriver.find_elements(*Locators.Constructor.CONTAINER_INGREDIENTS)

    assert len(found_elements) > 0, 'Ingredients container was not found'
    assert len(found_elements) == 1, 'Ambiguous results of searching for ingredients container'


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
    webdriver.get(Urls.BASE)

    js_click(webdriver, Locators.Header.ANCHOR_CONSTRUCTOR)

    js_click(
        webdriver,
        Locators.Constructor.get_span_ingredient_group(ingredient_group))

    js_wait_scrolled_into_view(
        webdriver,
        Locators.Constructor.get_title_ingredient_group(ingredient_group))

    assert js_check_scrolled_into_view(
        webdriver,
        Locators.Constructor.get_title_ingredient_group(ingredient_group))
