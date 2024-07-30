from pages.tables import Tables


def test_tables_sort(browser):
    tables_page = Tables(browser)

    tables_page.visit()
    tables_page.header_first_name.click()

    assert (tables_page.header_first_name.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-asc -cursor-pointer')
    tables_page.header_first_name.click()
    assert (tables_page.header_first_name.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-desc -cursor-pointer')

    tables_page.header_last_name.click()
    assert (tables_page.header_last_name.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-asc -cursor-pointer')
    tables_page.header_last_name.click()
    assert (tables_page.header_last_name.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-desc -cursor-pointer')

    tables_page.header_age.click()
    assert (tables_page.header_age.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-asc -cursor-pointer')
    tables_page.header_age.click()
    assert (tables_page.header_age.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-desc -cursor-pointer')

    tables_page.header_email.click()
    assert (tables_page.header_email.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-asc -cursor-pointer')
    tables_page.header_email.click()
    assert (tables_page.header_email.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-desc -cursor-pointer')

    tables_page.header_salary.click()
    assert (tables_page.header_salary.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-asc -cursor-pointer')
    tables_page.header_salary.click()
    assert (tables_page.header_salary.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-desc -cursor-pointer')

    tables_page.header_department.click()
    assert (tables_page.header_department.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-asc -cursor-pointer')
    tables_page.header_department.click()
    assert (tables_page.header_department.get_dom_attribute('class') ==
            'rt-th rt-resizable-header -sort-desc -cursor-pointer')
