import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from data import Data

DRIVERS = {
    "chrome": webdriver.Chrome,
    "firefox": webdriver.Firefox,
}

@pytest.fixture(params=DRIVERS.keys())
def driver(request):
    driver = DRIVERS[request.param]()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)

@pytest.fixture
def authorized_driver(driver):
    """Авторизует тестового пользователя (готовый креды из data.py) и возвращает driver."""
    login = LoginPage(driver)
    login.open_login()
    login.login(Data.TEST_EMAIL, Data.TEST_PASSWORD)
    login.wait_authorized()
    return driver

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def constructor_page(driver):
    return ConstructorPage(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)

@pytest.fixture
def authorized_constructor(authorized_driver, constructor_page):
    constructor_page.open_constructor()
    return constructor_page
