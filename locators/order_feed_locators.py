from selenium.webdriver.common.by import By

class OrderFeedLocators:
    HEADING = (By.XPATH, "//h1[contains(@class,'text_type_main-large')]")
  
    # XPath-шаблон числа счётчика по заголовку
    COUNTER_TPL = (
        By.XPATH,
        "//p[contains(normalize-space(), '{title}')]"
        "/following-sibling::p[contains(@class,'OrderFeed_number')]",
    )
    
    # XPath-шаблон карточки заказа с номером {number} в общей ленте
    ORDER_IN_FEED_TPL = (
        By.XPATH,
        "//a[contains(@class,'OrderHistory_link')][.//p[normalize-space()='#{number:05d}']]",
    )

    # XPath-шаблон номера заказа {number} в блоке «В работе»
    ORDER_IN_PROGRESS_TPL = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderListReady') or contains(@class,'OrderFeed_orderList')]"
        "/li[normalize-space()='{number:05d}']",
    )
    