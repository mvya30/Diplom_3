import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    
    @allure.step("Перейти в Ленту заказов")
    def click_order_feed(self):
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Перейти в Конструктор")
    def click_constructor(self):
        self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON) 
    
    @allure.step("Проверить отображение заголовка Конструктора")
    def is_constructor_visible(self):
        return self.is_element_displayed(MainPageLocators.CONSTRUCTOR_HEADER, timeout=5)
    
    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        return self.is_element_displayed(MainPageLocators.MODAL_WINDOW, timeout=5)

    @allure.step("Получить название ингредиента в деталях")
    def ingredient_name_in_details(self):
        self.visible(MainPageLocators.DETAILS_TITLE)
        return self.visible(MainPageLocators.DETAILS_NAME).text
    
    @allure.step("Кликнуть на ингредиент: {name}")
    def click_ingredient(self, name):
        locator = (MainPageLocators.INGREDIENT_BY_NAME[0], MainPageLocators.INGREDIENT_BY_NAME[1].format(name))
        self.js_click(locator)

    @allure.step("Окно с деталями ингредиента закрывается кликом по крестику")
    def close_modal(self):
         close_btn = self.wait.until(
             EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
         )
         self.driver.execute_script("arguments[0].click();", close_btn)
         self.wait_overlay_hidden()
         self.wait.until_not(
             EC.visibility_of_element_located(MainPageLocators.MODAL_WINDOW)
         )

    @allure.step("Перетащить ингредиент в корзину: {name}")
    def drag_ingredient_to_basket(self, name):
        source_locator = (
            MainPageLocators.INGREDIENT_CARD[0],
            MainPageLocators.INGREDIENT_CARD[1].format(name),
        )
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(MainPageLocators.BASKET)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            function fire(el, type) {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                el.dispatchEvent(event);
            }

            fire(source, 'dragstart');
            fire(target, 'dragenter');
            fire(target, 'dragover');
            fire(target, 'drop');
            fire(source, 'dragend');
        """, source, target)

    @allure.step("Получить счетчик ингредиента: {name}")
    def get_ingredient_counter(self, name: str):
        card_locator = (
            MainPageLocators.INGREDIENT_CARD_WITH_COUNTER[0],
            MainPageLocators.INGREDIENT_CARD_WITH_COUNTER[1].format(name),
        )
        ingredient_card = self.find_element_with_wait(card_locator)
        counter_element = ingredient_card.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter_element.text.strip())
          