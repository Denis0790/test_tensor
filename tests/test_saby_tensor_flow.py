from conftest import driver
from pages.saby_pages.contacts_page import ContactsPage
from pages.saby_pages.main_page import MainPage
from pages.tensor_page import TensorPage
import logging

logger = logging.getLogger(__name__)


def test_saby_navigation_to_contacts(driver) -> None:
    """
    Сценарий: переход из Саби в Тензор и проверка контента.
    1. Открывает Саби, переходит в раздел контактов
    2. Проверяет переход и кликает по баннеру Тензор
    3. Переключается на вкладку Тензор
    4. Проверяет блок Сила в людях и переходит в Подробнее
    5. Сверяет размеры всех фотографий в блоке Работаем
    """
    logger.info("Старт теста - Навигация Саби -> Тензор")
    main_page = MainPage(driver)
    contacts_page = ContactsPage(driver)

    main_page.open_main()
    main_page.go_to_contacts()

    assert "contacts" in driver.current_url, "Не перешли в раздел Контакты"

    contacts_page.click_tensor_banner()

    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    assert "tensor" in driver.current_url, "Сайт Тензор не открылся"

    tensor_page = TensorPage(driver)

    assert tensor_page.find_block_power_in_people(), "Нет блока 'Сила в людях'"

    tensor_page.go_to_about_in_block_power_in_people()

    assert driver.current_url == "https://tensor.ru/about", "Не перешли в раздел Подробнее"

    assert tensor_page.check_h_and_w_images_in_work(), \
        "Фотографии в блоке 'Работаем' имеют разные размеры"
    logger.info("Тест навигации и проверки картинок завершен успешно")
