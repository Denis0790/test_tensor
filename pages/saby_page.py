from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SabyPage(BasePage):
    URL = " https://saby.ru"
    CONTACTS = (By.XPATH, "//div[contains(@class, 'sbisru-MenuPopupTemplate__title')]//span[text()='Контакты']")
    GO_TO_CONTACTS = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu a[href='/contacts']")
    TENSOR_BANNER = (By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")

    def open_saby(self):
        self.open(SabyPage.URL)

    def hover_and_click_contacts(self):
        contacts_element = self.find(self.CONTACTS)

        actions = ActionChains(self.driver)
        actions.move_to_element(contacts_element).perform()

        self.click(self.GO_TO_CONTACTS)

    def click_banner_tensor(self):
        self.click(self.TENSOR_BANNER)