from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//header//a[contains(.,'Конструктор')]")
    FEED_LINK = (By.XPATH, "//header//a[contains(.,'Лента Заказов')]")
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

    @staticmethod
    def ingredient(ingredient_name):
        return (By.XPATH, f"//a[contains(.,'{ingredient_name}')]")

    @staticmethod
    def ingredient_counter(ingredient_name):
        return (
            By.XPATH,
            f"//a[contains(.,'{ingredient_name}')]//p[contains(@class,'counter_counter__num')]",
        )
