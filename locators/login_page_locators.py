from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//form//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//form//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//form//button[text()='Войти']")
