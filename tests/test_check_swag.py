from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_labs_page = SwagLabs(browser)

    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()


def test_username_field(browser):
    swag_labs_page = SwagLabs(browser)

    swag_labs_page.visit()
    assert swag_labs_page.exist_field('input#user-name')


def test_password_field(browser):
    swag_labs_page = SwagLabs(browser)

    swag_labs_page.visit()
    assert swag_labs_page.exist_field('input#password')
