from conftest import driver
from pages.saby_page import SabyPage
from pages.tensor_page import TensorPage


def test_saby_open_banner_tensor(driver):
    saby_page = SabyPage(driver)
    saby_page.open_saby()
    saby_page.hover_and_click_contacts()

    assert "contacts" in driver.current_url, "Не перешли в раздел контакты"

    saby_page.click_banner_tensor()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    assert "tensor" in driver.current_url, "Сайт Тензор не открылся"

    tensor_page = TensorPage(driver)

    assert tensor_page.find_block_power_in_people(), "Нет блока Сила в людях"

    tensor_page.go_to_about_in_block_power_in_people()

    assert "about" in driver.current_url, "Не перешли в раздел подробнее"

    assert tensor_page.check_h_and_w_images_in_work(), "Фотографии имеют разные размеры"