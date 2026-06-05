import urls
from data import BUN_NAME, FILLING_NAME
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators

    def open_main_page(self):
        self.open(urls.MAIN_PAGE)
        self.is_visible(self.locators.MAIN_HEADING)

    def constructor_is_opened(self):
        return self.is_visible(self.locators.MAIN_HEADING)

    def click_constructor(self):
        self.click(self.locators.CONSTRUCTOR_LINK)

    def click_feed(self):
        self.click(self.locators.FEED_LINK)

    def open_ingredient_details(self, ingredient_name=BUN_NAME):
        self.click(self.locators.ingredient(ingredient_name))

    def details_modal_is_opened(self):
        return self.is_visible(self.locators.INGREDIENT_DETAILS_TITLE)

    def close_modal(self):
        self.click(self.locators.MODAL_CLOSE_BUTTON)
        self.wait_invisible(self.locators.MODAL_OPENED)

    def add_bun_to_constructor(self):
        self.drag_and_drop(self.locators.ingredient(BUN_NAME), self.locators.DROP_ZONE)

    def add_filling_to_constructor(self):
        self.drag_and_drop(self.locators.ingredient(FILLING_NAME), self.locators.DROP_ZONE)

    def ingredient_counter(self, ingredient_name=BUN_NAME):
        return int(self.get_text(self.locators.ingredient_counter(ingredient_name)))

    def create_order(self):
        self.click(self.locators.ORDER_BUTTON)
        self.is_visible(self.locators.ORDER_NUMBER)

    def details_modal_is_closed(self):
        return self.is_absent(self.locators.INGREDIENT_DETAILS_TITLE)

    def create_order_for_user(self, user):
        from pages.login_page import LoginPage

        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.login(user["email"], user["password"])
        self.is_visible(self.locators.MAIN_HEADING)
        self.add_bun_to_constructor()
        self.add_filling_to_constructor()
        self.create_order()
