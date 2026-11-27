
import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from locators.main_page_locators import MainPageLocators
from data import Data, Urls

class ConstructorPage(BasePage):
    
    @allure.step("Открыть конструктор")
    def open_constructor(self):
        self.open(Urls.BASE_URL + Urls.MAIN_PATH)
    
    @allure.step("Получить локатор карточки ингредиента: {name}")
    def _ingredient_card_locator(self, name):
        by, template = ConstructorPageLocators.INGREDIENT_CARD_TPL
        return by, template.format(name=name)

    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self):
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self):
        self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перетащить «{name}» в заказ")
    def add_ingredient(self, name):
        self.drag_and_drop_js(self._ingredient_card_locator(name), ConstructorPageLocators.BASKET)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.js_click(ConstructorPageLocators.CLOSE_BUTTON)

    @allure.step("Собрать бургер и оформить заказ")
    def place_order(self):
        self.add_ingredient(Data.BUN)
        self.add_ingredient(Data.SAUCE)
        self.js_click(ConstructorPageLocators.ORDER_BUTTON)
        self.find_element_with_wait(ConstructorPageLocators.ORDER_NUMBER)
        self.wait_until(
            EC.invisibility_of_element_located(ConstructorPageLocators.ORDER_LOADER),
            "Лоадер не исчез после оформления заказа",
        )
        raw = self.get_text(ConstructorPageLocators.ORDER_NUMBER)
        return int(raw.lstrip("#"))
    