import re

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DownloadPage(BasePage):

    BTN_1C = (By.XPATH, "//div[@data-id='1c']")
    DOWNLOAD_LINK = (By.XPATH, "//div[not(contains(@class, 'ws-hidden'))]//a[contains(@href, 'Sbis1C_UF.epf')]")

    def go_to_1c_downloads(self) -> bool:
        """Жмем на Кнопку для 1с и явно ожидаем что вкладка открылась"""
        self.click(self.BTN_1C)
        return self.wait.until(
            lambda d: "controls-Checked__checked" in d.find_element(*self.BTN_1C).get_attribute("class")
        )

    def get_expected_size(self) -> float:
        """Брем размер файла из самой кнопки"""
        text = self.find(self.DOWNLOAD_LINK).text
        match = re.search(r"(\d+\.\d+)", text)
        return float(match.group(1)) if match else 0.0

    def click_download(self) -> None:
        """Просто клик по кнопке"""
        self.click(self.DOWNLOAD_LINK)
