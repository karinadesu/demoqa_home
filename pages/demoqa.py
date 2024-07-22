from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):

    # конструктор класса , это наша страница
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        # каждый элемент на странице создается внутри страницы по классе WebElement
        # тут всегда будет список элементов
        self.icon = WebElement(driver, '#app > header > a')
        self.bth_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer_text = WebElement(driver, '#app > footer')
        self.elements_text = WebElement(driver, '#app > div > div > div > div:nth-child(2)')
