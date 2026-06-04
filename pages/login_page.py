import urls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators

    def open_login_page(self):
        self.open(urls.LOGIN_PAGE)
        self.is_visible(self.locators.LOGIN_BUTTON)

    def login(self, email, password):
        self.type_text(self.locators.EMAIL_INPUT, email)
        self.type_text(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_BUTTON)
