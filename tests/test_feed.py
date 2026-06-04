import allure

from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.epic("Stellar Burgers UI")
@allure.feature("Лента заказов")
class TestFeed:
    @allure.title("После создания заказа счётчик Выполнено за все время увеличивается")
    def test_total_counter_increases_after_order_created(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        total_before = feed_page.total_counter()

        MainPage(driver).create_order_for_user(user)
        feed_page.open_feed_page()
        feed_page.wait_total_counter_greater_than(total_before)

        assert feed_page.total_counter() > total_before

    @allure.title("После создания заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_counter_increases_after_order_created(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        today_before = feed_page.today_counter()

        MainPage(driver).create_order_for_user(user)
        feed_page.open_feed_page()
        feed_page.wait_today_counter_greater_than(today_before)

        assert feed_page.today_counter() > today_before

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_created_order_number_appears_in_work_section(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        first_order_before = feed_page.first_order_number()

        MainPage(driver).create_order_for_user(user)
        feed_page.open_feed_page()
        feed_page.wait_first_order_number_changed(first_order_before)
        order_number = feed_page.first_order_number()
        assert feed_page.order_is_in_work(order_number)
