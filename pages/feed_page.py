import urls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    locators = FeedPageLocators

    def open_feed_page(self):
        self.open(urls.FEED_PAGE)
        self.is_visible(self.locators.FEED_HEADING)

    def feed_is_opened(self):
        return self.is_visible(self.locators.FEED_HEADING)

    def total_counter(self):
        return int(self.get_text(self.locators.TOTAL_COUNTER))

    def today_counter(self):
        return int(self.get_text(self.locators.TODAY_COUNTER))

    def first_order_number(self):
        return self.get_text(self.locators.FIRST_ORDER_NUMBER).replace("#", "").strip()

    def wait_first_order_number_changed(self, old_number):
        self.wait.until(lambda _: self.first_order_number() != old_number)

    def wait_total_counter_greater_than(self, value):
        self.wait.until(lambda _: self.total_counter() > value)

    def wait_today_counter_greater_than(self, value):
        self.wait.until(lambda _: self.today_counter() > value)

    def wait_order_in_work(self, order_number):
        self.is_visible(self.locators.order_in_work(order_number))

    def order_is_in_work(self, order_number):
        return self.is_visible(self.locators.order_in_work(order_number))
