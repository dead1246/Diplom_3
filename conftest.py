import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api_client import UserApi
from data import unique_user


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Браузер для UI-тестов",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        help="Запустить браузер в видимом режиме",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")

    if browser == "firefox":
        options = FirefoxOptions()
        if not headed:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1000")
        driver = webdriver.Chrome(options=options)

    driver.set_window_size(1440, 1000)
    yield driver
    driver.quit()


@pytest.fixture
def user():
    api = UserApi()
    payload = unique_user()
    response = api.create_user(payload)
    token = response.json().get("accessToken")

    yield payload

    if token:
        api.delete_user(token)
