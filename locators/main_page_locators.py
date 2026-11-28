from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//a[contains(@class,'AppHeader_header__link') and .//p[normalize-space()='Лента Заказов']]",
    )
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//a[contains(@class,'AppHeader_header__link') and .//p[normalize-space()='Конструктор']]",
    )
    CONSTRUCTOR_BUTTON_ACTIVE = (
        By.XPATH,
        "//a[contains(@class,'AppHeader_header__link_active') and .//p[normalize-space()='Конструктор']]",
    )

    MODAL_WINDOW = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]")
    MODAL_OVERLAY = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    
    DETAILS_TITLE = (By.XPATH, "//h2[normalize-space()='Детали ингредиента']")
    DETAILS_NAME = (
        By.XPATH,
        "//div[contains(@class,'Modal_modal__contentBox')]"
        "//p[contains(@class,'text_type_main-medium')]",
    )
    INGREDIENT_CARD_TPL = (By.XPATH, "//a[.//img[@alt='{name}']]")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class,'counter_counter__num')]")

    BASKET = (By.XPATH, "//div[contains(@class,'BurgerConstructor_basket')]")
