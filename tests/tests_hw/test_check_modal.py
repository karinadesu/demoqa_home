import time
import pytest
import urllib.request
from pages.modal_dialogs import ModalDialogPage
response = urllib.request.urlopen('https://demoqa.com/')


@pytest.mark.skipif(response.getcode() != 200, reason="page is unavailable")
def test_check_text(browser):
    modal_dialog = ModalDialogPage(browser)
    modal_dialog.visit()

    assert modal_dialog.small_modal_btn.exist()
    assert modal_dialog.large_modal_btn.exist()

    modal_dialog.small_modal_btn.click()
    time.sleep(2)
    assert modal_dialog.small_header_modal.get_text() == 'Small Modal'
    modal_dialog.close_small_modal_btn.click()
    time.sleep(2)
    assert not modal_dialog.small_header_modal.exist()

    modal_dialog.large_modal_btn.click()
    time.sleep(2)
    assert modal_dialog.large_header_modal.get_text() == 'Large Modal'
    modal_dialog.close_large_modal_btn.click()
    time.sleep(2)
    assert not modal_dialog.large_header_modal.exist()
