import os
from pages.saby_pages.download_page import DownloadPage
from pages.saby_pages.main_page import MainPage
from utils.file_utils import FileHelper
import logging

logger = logging.getLogger(__name__)


def test_download_sbis_plagin(driver):
    """Скачиваем ехе файл плагина для 1С"""
    logger.info("Старт теста - Скачивание плагина 1С")
    main_page = MainPage(driver)
    download_page = DownloadPage(driver)

    file_path = os.path.join(os.getcwd(), "Sbis1C_UF.epf")
    FileHelper.delete_if_exists(file_path)

    main_page.open_main()
    main_page.go_to_downloads()

    assert "download" in driver.current_url, "Не перешли в раздел Скачать локальные версии"

    assert download_page.go_to_1c_downloads(), "Не переключились на вкладку 1с"

    expected_size = download_page.get_expected_size()
    download_page.click_download()

    assert FileHelper.wait_for_download(file_path), "Файл не был загружен на диск"

    actual_size = FileHelper.get_file_size_mb(file_path)
    assert actual_size == expected_size, f"Размер не совпал! Сайт: {expected_size}, Диск: {actual_size}"

    FileHelper.delete_if_exists(file_path)
    logger.info("Тест скачивания завершен успешно")
