from selenium.webdriver.common.by import By

class OrderFeedLocators:
    HEADING = (By.XPATH, "//main//h1[normalize-space()='Лента заказов']")
  
    # XPath-шаблон числа счётчика по заголовку
    COUNTER_TPL = "//p[normalize-space()='{title}:']/following-sibling::p[1]"
    
    # XPath-шаблон карточки заказа с номером {number} в общей ленте
    ORDER_IN_FEED_TPL = (
        "//main//a[starts-with(@href, '/feed/')]"
        "//p[contains(@class, 'text_type_digits-default') "
        "and number(translate(substring-after(normalize-space(), '#'), ' ', '')) = {number}]"
    )

    # XPath-шаблон номера заказа {number} в блоке «В работе»
    ORDER_IN_PROGRESS_TPL = (
        "//ul[contains(@class, 'OrderFeed_orderListReady')]"
        "/li[number(normalize-space(.)) = {number}]"
    )
  