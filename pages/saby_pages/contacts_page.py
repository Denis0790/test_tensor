from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class ContactsPage(BasePage):
    """Класс для работы со страницей Контакты"""

    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    REGION_IN_CONTACTS = (By.CSS_SELECTOR,
                          ".sbisru-Contacts__relative .sbis_ru-Region-Chooser__text")
    PARTNERS = (By.CSS_SELECTOR, "[data-qa='item']")
    KAMCHATKA = (By.XPATH, "//span[@title='Камчатский край']")

    def click_tensor_banner(self) -> None:
        """Кликает по баннеру Тензор"""
        logger.info("Клик по баннеру Тензор")
        self.click(self.TENSOR_BANNER)

    def get_region_text(self) -> str:
        """Возвращает текущий регион в контактах"""
        logger.info("Определил текущий регион")
        return self.find(self.REGION_IN_CONTACTS).text

    def get_partner_text(self) -> str:
        """Возвращает текст первого партнера"""
        logger.info("Вернул текст первого партнера в списке")
        return self.find(self.PARTNERS).text

    def is_partners_list_visible(self) -> bool:
        """Проверяет, что список партнеров присутствует"""
        partners = self.find_elements(self.PARTNERS)
        logger.info("Проверка есть ли партнеры")
        return len(partners) > 0

    def get_partners_list_text(self) -> str:
        """Собирает текст всех партнеров в одну строку"""
        partners = self.find_elements(self.PARTNERS)
        logger.info("Собрал список всех парнеров со страницы")
        return "".join([partner.text for partner in partners])

    def change_region_to_kamchatka(self) -> None:
        """Меняет регион на Камчатский край"""
        logger.info("Меняем регион на камчатский край")
        self.click(self.REGION_IN_CONTACTS)
        self.click(self.KAMCHATKA)

        self.wait.until(
            EC.text_to_be_present_in_element(
                self.REGION_IN_CONTACTS,
                "Камчатский край"
            )
        )
        logger.info("Регион изменен на Камчатский Край")

    def is_region_correct(self, expected_region: str) -> bool:
        """Проверяет, что отображается ожидаемый регион"""
        logger.info("Отобразился ожидаемый регион")
        return self.get_region_text() == expected_region

    def check_region_and_partners_region(self) -> bool:
        """Проверяет соответствие региона и партнеров
        Сравнивает по первым буквам"""
        header_name = self.get_region_text().replace("г. ", "").split(" ")[0]
        search_root = header_name[:-2].lower()

        partner_text = self.get_partner_text().lower()
        logger.info("Выбранный регион соответствует региону указанному в партнерах")
        return search_root in partner_text
