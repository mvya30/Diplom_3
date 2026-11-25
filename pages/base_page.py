import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from data import Urls

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
       
    @allure.step("Открыть страницу: {url}")
    def open(self, url=None):
        self.driver.get(url or Urls.BASE_URL)

    @allure.step("Дождаться видимости элемента: {locator}")
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Дождаться кликабельности и нажать на элемент: {locator}")
    def click_element_with_wait(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Кликнуть через JS (обход перехвата): {locator}")
    def js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Дождаться отсутствия оверлея")
    def wait_overlay_hidden(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY))
    
    @allure.step("Проверить отображение элемента: {locator}")          
    def is_element_displayed(self, locator, timeout=5):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0 and elements[0].is_displayed()

    
    @allure.step("Дождаться условия: {message}")
    def wait_until(self, condition, message="Условие не выполнено"):
        return self.wait.until(condition, message)
        