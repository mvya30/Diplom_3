import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    @allure.step("Перейти в Ленту заказов")
    def click_order_feed(self):
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Перейти в Конструктор")
    def click_constructor(self):
        self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Проверить отображение активного раздела «Конструктор»")
    def is_constructor_visible(self):
        return self.is_element_displayed(MainPageLocators.CONSTRUCTOR_BUTTON_ACTIVE, timeout=5)

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        return self.is_element_displayed(MainPageLocators.MODAL_WINDOW, timeout=5)

    @allure.step("Получить название ингредиента в деталях")
    def ingredient_name_in_details(self):
        self.find_element_with_wait(MainPageLocators.DETAILS_TITLE)
        return self.get_text(MainPageLocators.DETAILS_NAME)

    @allure.step("Получить локатор карточки ингредиента: {name}")
    def _ingredient_card_locator(self, name):
        by, template = MainPageLocators.INGREDIENT_CARD_TPL
        return by, template.format(name=name)

    @allure.step("Кликнуть на ингредиент: {name}")
    def click_ingredient(self, name):
        self.js_click(self._ingredient_card_locator(name))

    @allure.step("Закрыть модальное окно ингредиента")
    def close_modal(self):
        self.js_click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_invisible(MainPageLocators.MODAL_WINDOW)

    @allure.step("Перетащить ингредиент в корзину: {name}")
    def drag_ingredient_to_basket(self, name):
        self.drag_and_drop_js(self._ingredient_card_locator(name), MainPageLocators.BASKET)

    @allure.step("Получить счётчик ингредиента: {name}")
    def get_ingredient_counter(self, name: str):
        card = self.find_element_with_wait(self._ingredient_card_locator(name))
        counter = card.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text.strip())
    