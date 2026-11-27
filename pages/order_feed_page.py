import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from data import Urls

class OrderFeedPage(BasePage):
    
    @allure.step("Открыть Ленту заказов")
    def open_feed(self):
        self.open(Urls.BASE_URL + Urls.ORDER_FEED_PATH)
        self.find_element_with_wait(OrderFeedLocators.HEADING)
    
    @allure.step("Получить локатор счётчика '{title}'")
    def _counter_locator(self, title):
        by, template = OrderFeedLocators.COUNTER_TPL
        return by, template.format(title=title)

    @allure.step("Получить локатор заказа №{number} в ленте")         
    def _order_in_feed_locator(self, number):
        by, template = OrderFeedLocators.ORDER_IN_FEED_TPL
        return by, template.format(number=number)
    
    @allure.step("Получить локатор заказа №{number} в работе")
    def _order_in_progress_locator(self, number):
        by, template = OrderFeedLocators.ORDER_IN_PROGRESS_TPL
        return by, template.format(number=number)
    
    @allure.step("Считать значение счётчика «{title}»")
    def counter(self, title):
        raw = self.get_text(self._counter_locator(title))
        digits = "".join(c for c in raw if c.isdigit())
        return int(digits) if digits else 0

    @allure.step("Дождаться увеличения счётчика «{title}»")
    def counter_increased(self, title, previous):
        return self.wait_until(
            lambda _: self.counter(title) > previous,
            f"Значение «{title}» не стало больше {previous}",
        )

    @allure.step("Найти заказ №{number} в ленте")
    def wait_for_order(self, number):
        self.find_element_with_wait(self._order_in_feed_locator(number))

    @allure.step("Найти заказ №{number} в разделе «В работе»")
    def order_is_in_progress(self, number):
        element = self.find_element_with_wait(self._order_in_progress_locator(number))
        return element.is_displayed()
    