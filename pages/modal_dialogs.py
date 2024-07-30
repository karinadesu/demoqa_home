from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.submenu_btns = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.home_page_icon = WebElement(driver, 'header > a > img')
        self.small_modal_btn = WebElement(driver, '#showSmallModal')
        self.close_small_modal_btn = WebElement(driver, '#closeSmallModal')
        self.large_modal_btn = WebElement(driver, '#showLargeModal')
        self.close_large_modal_btn = WebElement(driver, '#closeLargeModal')
        self.small_header_modal = WebElement(driver, '#example-modal-sizes-title-sm')
        self.large_header_modal = WebElement(driver, '#example-modal-sizes-title-lg')