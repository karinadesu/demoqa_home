from pages.links import LinksPage


def test_links(browser):
    links_page = LinksPage(browser)

    links_page.visit()
    assert links_page.home_link.exist()
    assert links_page.home_link.get_text() == 'Home'
    assert links_page.home_link.get_dom_attribute('href') == 'https://demoqa.com'
