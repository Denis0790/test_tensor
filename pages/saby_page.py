from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SabyPage(BasePage):
    """Класс для работы с главной страницей Saby и навигацией"""
    URL: str = " https://saby.ru"
    CONTACTS: tuple[str, str] = (By.XPATH, "//div[contains(@class, 'sbisru-MenuPopupTemplate__title')]//span[text()='Контакты']")
    GO_TO_CONTACTS: tuple[str, str] = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu a[href='/contacts']")
    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    REGION = ()

    def open_saby(self) -> None:
        """Открытвает главную страницу Саби"""
        self.open(SabyPage.URL)

    def hover_and_click_contacts(self) -> None:
        """Наводит курсор на Контакты (в хендлере) и кликает по ссылке перехода
                в раздел контактов"""
        contacts_element = self.find(self.CONTACTS)

        actions = ActionChains(self.driver)
        actions.move_to_element(contacts_element).perform()

        self.click(self.GO_TO_CONTACTS)

    def click_banner_tensor(self) -> None:
        """Кликает по баннеру Тензор"""
        self.click(self.TENSOR_BANNER)

