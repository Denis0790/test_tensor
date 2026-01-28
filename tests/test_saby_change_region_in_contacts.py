from conftest import driver
from pages.saby_page import SabyPage


def test_region_in_contacts(driver) -> None:
    """Проверяем что регион соответствует региону в Партнерах на странице Контакты"""

    saby_page = SabyPage(driver)
    saby_page.go_to_contact_page()

    assert "contacts" in driver.current_url, "Не перешли в раздел контакты"

    assert saby_page.is_region_correct("Ярославская обл."), (f"Ожидали Ярославскую обл., "
                                                             f"но определился {saby_page.get_region_text()}")

    assert saby_page.is_partners_list_visible(), "Список партнеров пуст или не загрузился"

    saby_page.change_region_kamchatka()

    assert "41-kamchatskij-kraj" in driver.current_url, "URL не обновился"
    assert "Камчатский край" in driver.title, "Title не обновился"
    assert "Камчатский край" == saby_page.get_region_text(), "Регион в шапке не Камчатка"

    assert saby_page.check_region_and_partners_region(), "Партнеры не соответствуют Камчатке"


