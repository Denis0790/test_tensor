from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TensorPage(BasePage):
    URL = "https://tensor.ru/"
    POWER_IN_PEOPLE_BLOCK =(By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    GO_TO_ABOUT_IN_BLOCK_POWER_IN_PEOPLE = (By.XPATH, "//p[text()='Сила в людях']/..//a[text()='Подробнее']")
    TEXT_WORK = (By.XPATH, "//h2[text()='Работаем']")
    IMAGES_IN_WORK = (By.XPATH, "//div[contains(@class, 'tensor_ru-About__block3')]//img")

    def open_tensor(self):
        self.open(self.URL)

    def find_block_power_in_people(self):
        block = self.find(self.POWER_IN_PEOPLE_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView();", block)
        return block.is_displayed()

    def go_to_about_in_block_power_in_people(self):
        self.click(self.GO_TO_ABOUT_IN_BLOCK_POWER_IN_PEOPLE)

    def scrol_and_get_images_in_work(self):
        text_work = self.find(self.TEXT_WORK)
        self.driver.execute_script("arguments[0].scrollIntoView();", text_work)

        return self.find_elements(self.IMAGES_IN_WORK)

    def check_h_and_w_images_in_work(self):
        images = self.scrol_and_get_images_in_work()

        if not images:
            raise Exception("Список изображений пуст!")

        first_h = images[0].get_attribute("height")
        first_w = images[0].get_attribute("width")

        for img in images:
            h = img.get_attribute("height")
            w = img.get_attribute("width")
            if h != first_h or w != first_w:
                return False
        return True

