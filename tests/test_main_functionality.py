import allure
from data import Data

@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_go_to_constructor(self, main_page):
        main_page.open()
        main_page.click_order_feed() 
        assert main_page.url_contains("feed")
        main_page.click_constructor()
        assert main_page.is_constructor_visible(), \
            "Не перешли на главную страницу (конструктор не виден)"
        
    @allure.title("Переход по клику на 'Лента заказов'")
    def test_go_to_order_feed(self, main_page):
        main_page.open()
        main_page.click_order_feed()
        assert main_page.url_contains("feed")

    @allure.title("Клик по ингредиенту открывает модальное окно")
    def test_open_ingredient_modal(self, main_page):
        main_page.open()
        main_page.click_ingredient(Data.BUN)
        assert main_page.is_modal_opened(), "Модальное окно не открылось"

    @allure.title("Модальное окно закрывается по крестику")
    def test_close_ingredient_modal(self, main_page):
        main_page.open()
        main_page.click_ingredient(Data.BUN)
        assert main_page.is_modal_opened(), "Модальное окно не открылось"
        main_page.close_modal()
        assert not main_page.is_modal_opened(), "Модальное окно не закрылось"

    @allure.title("Счётчик ингредиента увеличивается при перетаскивании в заказ")
    def test_ingredient_counter_increases(self, main_page):
        main_page.open()
        name = Data.BUN
        main_page.drag_ingredient_to_basket(name)
        new_counter = main_page.get_ingredient_counter(name)

        assert new_counter == 2, "Счётчик не увеличился после перетаскивания булки"
