from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    BASKET = (By.XPATH, "//div[contains(@class,'BurgerConstructor_basket')]")
    
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    ORDER_NUMBER = (By.CSS_SELECTOR, "[class^='Modal_modal__contentBox__'] .text_type_digits-large")
    ORDER_LOADER = (By.CSS_SELECTOR, "[class*='Modal_modal_opened__'] img[alt='loading animation']")

    INGREDIENT_CARD_TPL = (By.XPATH, "//a[.//img[@alt='{name}']]")
  