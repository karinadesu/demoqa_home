from components.components import WebElement
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.submit_btn = WebElement(driver, '#submit')
        self.output_name = WebElement(driver, '#output #name')
        self.output_current_address = WebElement(driver, '#output #currentAddress')



