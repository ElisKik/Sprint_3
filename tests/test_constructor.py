# -*- coding: utf8 -*-

import pytest

from selenium.webdriver import Chrome as WebDriver

from locators import Locators
from urls import Urls
from waits import wait_visible

def test_go_to_constructor_from_logo(webdriver: WebDriver):
    webdriver.get(Urls.BASE)

    webdriver.find_element(*Locators.Main.ANCHOR_LOGO).click()

    found_elements = webdriver.find_elements(*Locators.Constructor.CONTAINER_INGREDIENTS)

    assert len(found_elements) > 0, 'Ingredients container was not found'
    assert len(found_elements) == 1, 'Ambiguous results of searching for ingredients container'

def test_go_to_constructor_from_header(webdriver: WebDriver):
    webdriver.get(Urls.BASE)

    webdriver.find_element(*Locators.Header.ANCHOR_CONSTRUCTOR).click()

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
def test_go_to_ingredient_group(webdriver: WebDriver, ingredient_group: str):
    webdriver.get(Urls.BASE)

    webdriver.find_element(*Locators.Header.ANCHOR_CONSTRUCTOR).click()

    selected_ingredient_groups = webdriver.find_elements(*Locators.Constructor.get_div_selected_ingredient_group(ingredient_group))

    # Skip clicking on already selected ingredient group tab:
    if len(selected_ingredient_groups) == 0:
        webdriver.find_element(*Locators.Constructor.get_span_ingredient_group(ingredient_group)).click()

    ingredient_group_visible = wait_visible(
        webdriver,
        Locators.Constructor.get_title_ingredient_group(ingredient_group))

    assert ingredient_group_visible, f'Selected ingredient group {ingredient_group} is not visible'
