from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    BASKET = (By.CSS_SELECTOR, "section[class^='BurgerConstructor_basket__']")
    
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close__']")
    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    ORDER_NUMBER = (By.CSS_SELECTOR, "[class^='Modal_modal__contentBox__'] .text_type_digits-large")
    ORDER_LOADER = (By.CSS_SELECTOR, "[class*='Modal_modal_opened__'] img[alt='loading animation']")

    INGREDIENT_CARD_TPL = "//main//a[img[@alt='{name}']]"
    