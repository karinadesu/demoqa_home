from pages.text_box_page import TextBoxPage


def test_text_box(browser):
    text_box_page = TextBoxPage(browser)

    name = 'Evan Peters'
    address = 'California'

    text_box_page.visit()
    text_box_page.full_name.send_keys(name)
    text_box_page.current_address.send_keys(address)
    text_box_page.submit_btn.click_force()
    assert text_box_page.output_name.get_text() == 'Name:' + name
    assert text_box_page.output_current_address.get_text() == 'Current Address :' + address
