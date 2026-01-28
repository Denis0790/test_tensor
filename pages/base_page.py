from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url: str) -> None:
        """Открыть указанный URL"""
        self.driver.get(url)

    def find(self, locator: tuple[str, str]) -> WebElement:
        """Найти элемент по локатору с ожиданием его появления"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        """Дождаться появления элемента и кликнуть по нему"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.click()

    def switch_to_new_window(self) -> None:
        """Дождаться появления нового окна и перейти на него"""
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def find_elements(self, locator: tuple[str, str]) -> List[WebElement]:
        """Найти все элементы по локатору с ожиданием их видимости"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
