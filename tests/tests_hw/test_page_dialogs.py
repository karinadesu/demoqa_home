import time
from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogPage


def test_modal_elements(browser):
    modal_dialog = ModalDialogPage(browser)

    modal_dialog.visit()
    assert modal_dialog.submenu_btns.check_count_elements(5)


def test_navigation_modal(browser):
    modal_dialog = ModalDialogPage(browser)
    demoqa_page = DemoQa(browser)

    modal_dialog.visit()
    modal_dialog.refresh()
    modal_dialog.home_page_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()
    assert demoqa_page.equal_url()
    browser.set_window_size(1000, 1000)
    time.sleep(2)
