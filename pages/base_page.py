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

    @allure.step("Получить текущий URL")
    def current_url(self):
        return self.driver.current_url
    
    @allure.step("Проверить, что URL содержит: {substring}")
    def url_contains(self, substring):
        return substring in self.driver.current_url

    @allure.step("Дождаться видимости элемента: {locator}")
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Дождаться присутствия элемента: {locator}")
    def wait_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Дождаться кликабельности элемента: {locator}")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Дождаться отсутствия элемента: {locator}")
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться исчезновения оверлея")
    def wait_overlay_hidden(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY))

    @allure.step("Дождаться условия: {message}")
    def wait_until(self, condition, message="Условие не выполнено"):
        return self.wait.until(condition, message)
    
    @allure.step("Клик по элементу: {locator}")
    def click_element_with_wait(self, locator):
        self.wait_clickable(locator).click()

    @allure.step("JS-клик по элементу: {locator}")
    def js_click(self, locator):
        element = self.wait_presence(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Проверить отображение элемента: {locator}")          
    def is_element_displayed(self, locator, timeout=5):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step("Перетащить элемент в элемент")
    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            
            function fire(el, type) {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                el.dispatchEvent(event);
            }
            
            fire(source, 'dragstart');
            fire(target, 'dragenter');
            fire(target, 'dragover');
            fire(target, 'drop');
            fire(source, 'dragend');
            """,
            source,
            target,
        )
        