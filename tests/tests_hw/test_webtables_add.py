from pages.tables import Tables
import time


def test_add_tables(browser):
    tables_page = Tables(browser)

    tables_page.visit()
    tables_page.btn_add.click()
    time.sleep(3)
    assert tables_page.modal_dialog.visible()
    tables_page.btn_submit_dialog.click_force()
    time.sleep(2)

    tables_page.input_first_name.send_keys('Evan')
    tables_page.input_last_name.send_keys('Peters')
    tables_page.input_email.send_keys('evan_peters@yahoo.com')
    tables_page.input_age.send_keys('36')
    tables_page.input_salary.send_keys('1999')
    tables_page.input_department.send_keys('IT Department')

    tables_page.btn_submit_dialog.click_force()
    time.sleep(2)

    assert tables_page.row_first_name.get_text() == 'Evan'
    assert tables_page.row_last_name.get_text() == 'Peters'
    assert tables_page.row_email.get_text() == 'evan_peters@yahoo.com'
    assert tables_page.row_age.get_text() == '36'
    assert tables_page.row_salary.get_text() == '1999'
    assert tables_page.row_department.get_text() == 'IT Department'

    tables_page.added_row_edit.click()
    time.sleep(2)
    assert tables_page.modal_dialog.visible()

    assert tables_page.input_first_name.get_dom_attribute('value') == 'Evan'
    assert tables_page.input_last_name.get_dom_attribute('value') == 'Peters'
    assert tables_page.input_email.get_dom_attribute('value') == 'evan_peters@yahoo.com'
    assert tables_page.input_age.get_dom_attribute('value') == '36'
    assert tables_page.input_salary.get_dom_attribute('value') == '1999'
    assert tables_page.input_department.get_dom_attribute('value') == 'IT Department'
    time.sleep(2)
    tables_page.input_first_name.clear()
    # assert tables_page.input_first_name.get_dom_attribute('value') == ''
    time.sleep(2)
    tables_page.input_first_name.send_keys('John')
    tables_page.btn_submit_dialog.click_force()
    time.sleep(2)
    assert tables_page.row_first_name.get_text() == 'EvanJohn'
    tables_page.added_row_delete.click()
    assert not tables_page.added_row_edit.exist()






