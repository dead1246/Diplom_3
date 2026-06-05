from selenium.webdriver.common.by import By


class FeedPageLocators:
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

    @staticmethod
    def order_in_work(order_number):
        return (
            By.XPATH,
            f"//*[contains(@class,'OrderFeed_orderStatusBox')]//li[normalize-space()='{order_number}']",
        )
