from selenium.webdriver.common.by import By

import urls
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//form//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//form//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//form//button[text()='Войти']")

    def open_login_page(self):
        self.open(urls.LOGIN_PAGE)
        self.is_visible(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
