from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class SabyPage(BasePage):
    """Класс для работы с главной страницей Saby и навигацией"""
    URL: str = " https://saby.ru"
    CONTACTS: tuple[str, str] = (By.XPATH, "//div[contains(@class, 'sbisru-MenuPopupTemplate__title')]//span[text()='Контакты']")
    GO_TO_CONTACTS: tuple[str, str] = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu a[href='/contacts']")
    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    REGION_IN_CONTACTS = (By.CSS_SELECTOR, ".sbisru-Contacts__relative .sbis_ru-Region-Chooser__text")
    REGION_IN_PARTNERS = (By.CSS_SELECTOR, "[data-qa='item']")
    KAMCHATKA = (By.XPATH, "//span[@title='Камчатский край']")

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

    def go_to_contact_page(self) -> None:
        """Открывает Саби и переходит в контакты"""
        self.open_saby()
        self.hover_and_click_contacts()

    def get_region_text(self) -> str:
        return self.find(self.REGION_IN_CONTACTS).text

    def get_region_text_in_partners(self) -> str:
        return self.find(self.REGION_IN_PARTNERS).text

    def is_region_correct(self, expected_region: str) -> bool:
        """Проверяет, что отображается ожидаемый регион"""
        actual_region = self.get_region_text()
        return actual_region == expected_region

    def is_partners_list_visible(self) -> bool:
        """Проверяет, что блок с партнерами присутствует на странице и не пуст"""
        partners = self.find_elements(self.REGION_IN_PARTNERS)
        return len(partners) > 0

    def change_region_kamchatka(self) -> None:
        """Нажимаем на свой регион и выбираем регион Камчатка"""
        self.click(self.REGION_IN_CONTACTS)
        self.click(self.KAMCHATKA)
        self.wait.until(
            EC.text_to_be_present_in_element(self.REGION_IN_CONTACTS, "Камчатский край")
        )

    def check_region_and_partners_region(self)-> bool:
        """Проверяет текущий регион с регионом представленных партнеров на странице Контакты
        по первым буквам сравнивает и возвращает TRUE если совпало FALSE если нет"""
        header_name = self.get_region_text().replace("г. ", "").split(" ")[0]
        search_root = header_name[:-2].lower()

        partner_text = self.get_region_text_in_partners().lower()

        return search_root in partner_text

