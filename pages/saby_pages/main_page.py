from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class MainPage(BasePage):
    """Класс для работы с главной страницей Saby"""

    URL: str = "https://saby.ru"
    CONTACTS: tuple[str, str] = (By.XPATH,
        "//div[contains(@class, 'sbisru-MenuPopupTemplate__title')]//span[text()='Контакты']")
    GO_TO_CONTACTS: tuple[str, str] = (By.CSS_SELECTOR,
        ".sbisru-Header-ContactsMenu a[href='/contacts']")
    GO_TO_DOWNLOADS_PLAGIN: tuple[str, str] = (By.LINK_TEXT, "Скачать локальные версии")

    def open_main(self) -> None:
        """Открывает главную страницу Saby"""
        self.open(self.URL)

    def go_to_contacts(self) -> None:
        """Наводит курсор на Контакты и переходит в раздел Контакты"""
        contacts_element = self.find(self.CONTACTS)

        actions = ActionChains(self.driver)
        actions.move_to_element(contacts_element).perform()

        self.click(self.GO_TO_CONTACTS)

    def go_to_downloads(self):
        footer_element = self.find(self.GO_TO_DOWNLOADS_PLAGIN)
        self.driver.execute_script("arguments[0].scrollIntoView();", footer_element)
        self.click(self.GO_TO_DOWNLOADS_PLAGIN)
