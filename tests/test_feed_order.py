import allure
from data import Data

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("После оформления заказа увеличивается счётчик «Выполнено за всё время»")
    def test_total_counter_increases(self, authorized_constructor, order_feed_page):
        counter=Data.TOTAL_COUNTER
        constructor = authorized_constructor
        feed = order_feed_page

        constructor.go_to_feed()
        feed.open_feed()
        before = feed.counter(counter)

        constructor.go_to_constructor()
        constructor.open_constructor()

        number = constructor.place_order()
        constructor.close_modal()

        constructor.go_to_feed()
        feed.open_feed()
        feed.wait_for_order(number)

        assert feed.counter_increased(counter, before), (
            f"Счётчик «{counter}» не увеличился: было {before}"
        )

    @allure.title("После оформления заказа увеличивается счётчик «Выполнено за сегодня»")
    def test_today_counter_increases(self, authorized_constructor, order_feed_page):
        counter=Data.TODAY_COUNTER
        constructor = authorized_constructor
        feed = order_feed_page

        constructor.go_to_feed()
        feed.open_feed()
        before = feed.counter(counter)

        constructor.go_to_constructor()
        constructor.open_constructor()

        number = constructor.place_order()
        constructor.close_modal()

        constructor.go_to_feed()
        feed.open_feed()
        feed.wait_for_order(number)

        assert feed.counter_increased(counter, before), (
            f"Счётчик «{counter}» не увеличился: было {before}"
        )

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    def test_new_order_is_in_progress(self, authorized_constructor, order_feed_page):
        constructor = authorized_constructor
        feed = order_feed_page

        number = constructor.place_order()
        constructor.close_modal()

        constructor.go_to_feed()
        feed.open_feed()

        assert feed.order_is_in_progress(number), (
            f"Заказ №{number} не появился в разделе «В работе»"
        )
        