from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

import urls
from pages.base_page import BasePage


class FeedPage(BasePage):
    FEED_HEADING = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p",
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    FIRST_ORDER_NUMBER = (By.XPATH, "//main//li[starts-with(.,'#')][1]//p")

    def open_feed_page(self):
        self.open(urls.FEED_PAGE)
        self.is_visible(self.FEED_HEADING)

    def total_counter(self):
        return int(self.get_text(self.TOTAL_COUNTER))

    def today_counter(self):
        return int(self.get_text(self.TODAY_COUNTER))

    def first_order_number(self):
        return self.get_text(self.FIRST_ORDER_NUMBER).replace("#", "").strip()

    def wait_first_order_number_changed(self, old_number):
        self.wait.until(lambda _: self.first_order_number() != old_number)

    def wait_total_counter_greater_than(self, value):
        self.wait.until(lambda _: self.total_counter() > value)

    def wait_today_counter_greater_than(self, value):
        self.wait.until(lambda _: self.today_counter() > value)

    def wait_order_in_work(self, order_number):
        locator = (
            By.XPATH,
            f"//*[contains(@class,'OrderFeed_orderStatusBox')]//li[normalize-space()='{order_number}']",
        )
        self.wait.until(ec.visibility_of_element_located(locator))
