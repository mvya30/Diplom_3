import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.constructor_page_locators import ConstructorPageLocators
from data import Urls


class LoginPage(BasePage):
    
    @allure.step("Открыть страницу входа")
    def open_login(self):
        self.open(Urls.BASE_URL + Urls.LOGIN_PATH)

    @allure.step("Войти под тестовым пользователем")
    def login(self, email, password):
        self.find_element_with_wait(LoginPageLocators.EMAIL).send_keys(email)
        self.find_element_with_wait(LoginPageLocators.PASSWORD).send_keys(password)
        self.js_click(LoginPageLocators.SUBMIT)

    @allure.step("Дождаться успешной авторизации")
    def wait_authorized(self):
        return self.find_element_with_wait(ConstructorPageLocators.ORDER_BUTTON)
    