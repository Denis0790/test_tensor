from typing import List
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class TensorPage(BasePage):
    """Класс для работы с сайтом Тензор"""
    URL = "https://tensor.ru/"
    POWER_IN_PEOPLE_BLOCK = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    GO_TO_ABOUT_IN_BLOCK_POWER_IN_PEOPLE = (By.XPATH, "//p[text()='Сила в людях']/..//a[text()='Подробнее']")
    TEXT_WORK = (By.XPATH, "//h2[text()='Работаем']")
    IMAGES_IN_WORK = (By.XPATH, "//div[contains(@class, 'tensor_ru-About__block3')]//img")

    def open_tensor(self) -> None:
        """Открывает главную страницу Тензор"""
        logger.info("Открыли главную страницу Тензор")
        self.open(self.URL)

    def find_block_power_in_people(self) -> bool:
        """Находит блок Сила в людях, скролит к нему и проверяет отображение"""
        block = self.find(self.POWER_IN_PEOPLE_BLOCK)
        logger.info("Скролим до блока Сила в людях...")
        self.driver.execute_script("arguments[0].scrollIntoView();", block)
        logger.info("Блок на месте")
        return block.is_displayed()

    def go_to_about_in_block_power_in_people(self) -> None:
        """Кликает по Подробнее в блоке Сила в людях"""
        logger.info("Кликаем по кнопке подробнее")
        self.click(self.GO_TO_ABOUT_IN_BLOCK_POWER_IN_PEOPLE)

    def scrol_and_get_images_in_work(self) -> List[WebElement]:
        """Скроллит до раздела Работаем и возвращает список всех изображений"""
        text_work = self.find(self.TEXT_WORK)
        logger.info("Скролим до раздела Работаем...")
        self.driver.execute_script("arguments[0].scrollIntoView();", text_work)
        logger.info("Взяли список изображений из раздела Работаем")
        return self.find_elements(self.IMAGES_IN_WORK)

    def check_h_and_w_images_in_work(self) -> bool:
        """Проверяет что все изображения одинаковой высоты и ширины.
        Возвращает TRUE если совпали, иначе FALSE"""
        images = self.scrol_and_get_images_in_work()

        if not images:
            logger.info("Изображения не найдены")
            return False

        first_h = images[0].get_attribute("height")
        first_w = images[0].get_attribute("width")

        for img in images:
            h = img.get_attribute("height")
            w = img.get_attribute("width")
            if h != first_h or w != first_w:
                logger.info("Размер изображений не совпадает!")
                return False
        logger.info("Размер изображений совпал")
        return True
