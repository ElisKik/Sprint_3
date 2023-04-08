"""
Predefined project-specific reusable locators.
"""

from selenium.webdriver.common.by import By

from aliases import Locator

class Locators:
    """
    Predefined reusable locators.
    """

    class Header:
        """
        Locators at page header.
        """

        ANCHOR_CONSTRUCTOR: Locator = (By.XPATH, './/header/nav/ul/li[1]/a')
        """
        Link leads to page that contains ingredient constructor.
        """

    class Main:
        """
        Locators of main page.
        """

        ANCHOR_ACCOUNT: Locator = (By.XPATH, './/a[@href="/account"]')
        """
        Link leads to account login page or already registered profile.
        """

        ANCHOR_LOGO: Locator = (By.XPATH, './/a[@href="/" and @class="active"]')
        """
        Link leads to account login page or already registered profile.
        """

        BUTTON_LOGIN: Locator = (By.XPATH, './/div[starts-with(@class,"BurgerConstructor_basket__container")]/button')
        """
        Button leads to account login.
        """

    class Account:
        """
        Locators of account page.
        """

        ANCHOR_REGISTER: Locator = (By.XPATH, './/a[@href="/register"]')
        """
        Link leads to account registration form.
        """

        ANCHOR_RECOVER_PASSWORD: Locator = (By.XPATH, './/a[@href="/forgot-password"]')
        """
        Link leads to password recovery.
        """

    class Registration:
        INPUT_NAME: Locator = (By.XPATH, './/form/fieldset[1]/div/div/input')
        """
        Input field for real name of user.
        """

        INPUT_EMAIL: Locator = (By.XPATH, './/form/fieldset[2]/div/div/input')
        """
        Input field for email of user.
        """

        INPUT_PASSWORD: Locator = (By.XPATH, './/form/fieldset[3]/div/div/input')
        """
        Input field for password of user.
        """

        PARAGRAPH_PASSWORD_ERROR: Locator = (By.XPATH, './/form/fieldset[3]/div/p[starts-with(@class,"input__error")]')
        """
        Caption for invalid password entered.
        """

        BUTTON_REGISTER: Locator = (By.XPATH, './/form/button')
        """
        Button submits account registration form.
        """

    class Login:
        """
        Locators of login form page.
        """

        INPUT_EMAIL: Locator = (By.XPATH, './/form/fieldset[1]/div/div/input')
        """
        Input field for email of user.
        """

        INPUT_PASSWORD: Locator = (By.XPATH, './/form/fieldset[2]/div/div/input')
        """
        Input field for password of user.
        """

        BUTTON_LOGIN: Locator = (By.XPATH, './/form/button')
        """
        Button submits account login form.
        """

        FORM_LOGIN: Locator = (By.XPATH, './/form[starts-with(@class,"Auth_form")]')
        """
        Form of login form page.
        """

    class PasswordRecovery:
        """
        Locators of password recovery page.
        """

        ANCHOR_LOGIN: Locator = (By.XPATH, './/a[@href="/login"]')
        """
        Link leads to account login.
        """

    class Constructor:
        """
        Locators of ingredient constructor section.
        """

        CONTAINER_INGREDIENTS: Locator = (By.XPATH, './/div[starts-with(@class,"BurgerIngredients_ingredients__menuContainer")]')
        """
        Contains ingredient list items.
        """

        @staticmethod
        def get_div_selected_ingredient_group(ingredient_group: str) -> Locator:
            """
            Tab container of currently selected ingredient group.
            """
            return (By.XPATH, f'.//div[contains(@class, "current")]//span[text()="{ingredient_group}"]')

        @staticmethod
        def get_span_ingredient_group(ingredient_group: str) -> Locator:
            """
            Tab of ingredient group.
            """
            return (By.XPATH, f'.//span[text()="{ingredient_group}"]')

        @staticmethod
        def get_title_ingredient_group(ingredient_group: str) -> Locator:
            """
            Title of ingredient group as scroll item.
            """
            return (By.XPATH, f'.//h2[text()="{ingredient_group}"]')

    class Profile:
        """
        Locators of authorized user profile page.
        """

        BUTTON_LOGOUT: Locator = (By.XPATH, './/main/div/nav/ul/li[3]/button')
        """
        Button performs logout.
        """

        PARAGRAPH_DESCRIPTION = (By.XPATH, './/p[starts-with(@class, "Account_text")]')
        """
        Account actions description.
        """
