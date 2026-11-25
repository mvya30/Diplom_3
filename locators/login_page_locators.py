from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, "form input[name='name']")
    PASSWORD = (By.CSS_SELECTOR, "form input[type='password']")
    SUBMIT = (By.XPATH, "//form//button[normalize-space()='Войти']")

    PLACE_ORDER = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
