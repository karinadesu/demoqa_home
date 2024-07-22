from pages.demoqa import DemoQa
from pages.elements import ElementsPage


def test_check_text(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()

    assert demo_qa_page.icon.exist()
    assert demo_qa_page.footer_text.check_text('© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')


def test_check_text_elements(browser):
    demo_qa_page = DemoQa(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.bth_elements.exist()

    demo_qa_page.bth_elements.click()
    assert el_page.equal_url()
    assert demo_qa_page.elements_text.check_text('Please select an item from left to start practice.')


def test_page_elements(browser):
    el_page = ElementsPage(browser)

    el_page.visit()
    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()
