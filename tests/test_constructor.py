import allure

from data import BUN_NAME
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.epic("Stellar Burgers UI")
@allure.feature("Основная функциональность")
class TestConstructor:
    @allure.title("Переход по клику на Конструктор")
    def test_click_constructor_opens_constructor_page(self, driver):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        feed_page.open_feed_page()

        main_page.click_constructor()

        main_page.wait_url_contains("/")
        assert main_page.is_visible(main_page.MAIN_HEADING)

    @allure.title("Переход по клику на Ленту заказов")
    def test_click_feed_opens_feed_page(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.open_main_page()

        main_page.click_feed()

        main_page.wait_url_contains("/feed")
        assert feed_page.is_visible(feed_page.FEED_HEADING)

    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.open_ingredient_details(BUN_NAME)

        assert main_page.is_visible(main_page.INGREDIENT_DETAILS_TITLE)

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_details_modal_closes_by_cross_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_ingredient_details(BUN_NAME)

        main_page.close_modal()

        assert not driver.find_elements(*main_page.INGREDIENT_DETAILS_TITLE)

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = main_page.ingredient_counter(BUN_NAME)

        main_page.add_bun_to_constructor()

        assert main_page.ingredient_counter(BUN_NAME) > counter_before
