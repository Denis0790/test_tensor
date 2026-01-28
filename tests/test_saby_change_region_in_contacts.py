from conftest import driver
from pages.saby_pages.contacts_page import ContactsPage
from pages.saby_pages.main_page import MainPage


def test_region_in_contacts(driver) -> None:
    """Проверяем, что регион соответствует региону в Партнерах на странице Контакты"""

    main_page = MainPage(driver)
    contacts_page = ContactsPage(driver)

    main_page.open_main()
    main_page.go_to_contacts()

    assert "contacts" in driver.current_url, "Не перешли в раздел Контакты"

    assert contacts_page.is_region_correct("Ярославская обл."), (
        f"Ожидали Ярославскую обл., "
        f"но определился {contacts_page.get_region_text()}"
    )

    assert contacts_page.is_partners_list_visible(), "Список партнеров пуст или не загрузился"
    old_partners_list = contacts_page.get_partners_list_text()

    contacts_page.change_region_to_kamchatka()
    new_partners_list = contacts_page.get_partners_list_text()

    assert old_partners_list != new_partners_list, \
        "Список партнеров не изменился после смены региона!"

    assert "41-kamchatskij-kraj" in driver.current_url, "URL не обновился"
    assert "Камчатский край" in driver.title, "Title не обновился"
    assert contacts_page.get_region_text() == "Камчатский край", \
        "Регион в шапке не Камчатка"

    assert contacts_page.check_region_and_partners_region(), \
        "Партнеры не соответствуют Камчатке"


