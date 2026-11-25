from selenium.webdriver.common.by import By
class MainPageLocators:
    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")

    INGREDIENT_BY_NAME = (By.XPATH, "//p[text()='{}']")
    INGREDIENT_CARD = (By.XPATH, "//a[.//p[text()='{}']]")
    INGREDIENT_CARD_WITH_COUNTER = (By.XPATH, "//p[text()='{}']/ancestor::a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class*='counter_counter']")
    
    # Модальное окно
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")
    
    # Конструктор (для сборки заказа)
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")

    DETAILS_TITLE = (By.XPATH, "//h2[normalize-space()='Детали ингредиента']")
    DETAILS_NAME = (By.CSS_SELECTOR, "[class^='Modal_modal__contentBox__'] > p")