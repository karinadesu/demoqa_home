import time
from pages.accordian import AccordianPage


def test_visible_accordian(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    assert accordian_page.section_content_first.visible()

    accordian_page.section_heading_first.click()
    time.sleep(2)
    assert not accordian_page.section_content_first.visible()


def test_visible_accordian_default(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    assert not accordian_page.section_content_second_part_one.visible()
    assert not accordian_page.section_content_second_part_two.visible()
    assert not accordian_page.section_content_third.visible()
