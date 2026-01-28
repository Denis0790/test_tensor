from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator: tuple[str, str]):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple[str, str]):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.click()

    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def find_elements(self, locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
