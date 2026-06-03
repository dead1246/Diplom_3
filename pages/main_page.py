from selenium.webdriver.common.by import By

import urls
from data import BUN_NAME, FILLING_NAME
from pages.base_page import BasePage


class MainPage(BasePage):
    CONSTRUCTOR_LINK = (By.XPATH, "//header//a[contains(.,'Конструктор')]")
    FEED_LINK = (By.XPATH, "//header//a[contains(.,'Лента Заказов')]")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    MAIN_HEADING = (By.XPATH, "//h1[text()='Соберите бургер']")
    MODAL_OPENED = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]//button[contains(@class,'Modal_modal__close')]",
    )
    INGREDIENT_DETAILS_TITLE = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]//h2[text()='Детали ингредиента']",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]//p[text()='идентификатор заказа']/preceding-sibling::h2",
    )
    DROP_ZONE = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor_basket')]",
    )

    def open_main_page(self):
        self.open(urls.MAIN_PAGE)
        self.is_visible(self.MAIN_HEADING)

    def click_constructor(self):
        self.click(self.CONSTRUCTOR_LINK)

    def click_feed(self):
        self.click(self.FEED_LINK)

    def open_ingredient_details(self, ingredient_name=BUN_NAME):
        self.click(self.ingredient(ingredient_name))

    def close_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)
        self.wait_invisible(self.MODAL_OPENED)

    def add_bun_to_constructor(self):
        self.drag_and_drop(self.ingredient(BUN_NAME), self.DROP_ZONE)

    def add_filling_to_constructor(self):
        self.drag_and_drop(self.ingredient(FILLING_NAME), self.DROP_ZONE)

    def ingredient_counter(self, ingredient_name=BUN_NAME):
        return int(self.get_text(self.ingredient_counter_locator(ingredient_name)))

    def create_order(self):
        self.click(self.ORDER_BUTTON)
        self.is_visible(self.ORDER_NUMBER)

    @staticmethod
    def ingredient(ingredient_name):
        return (By.XPATH, f"//a[contains(.,'{ingredient_name}')]")

    @staticmethod
    def ingredient_counter_locator(ingredient_name):
        return (
            By.XPATH,
            f"//a[contains(.,'{ingredient_name}')]//p[contains(@class,'counter_counter__num')]",
        )
