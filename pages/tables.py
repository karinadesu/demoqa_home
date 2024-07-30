from components.components import WebElement
from pages.base_page import BasePage


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.modal_dialog = WebElement(driver, '.modal-content')
        self.btn_delete_row = WebElement(driver, '[title="Delete"]')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit_dialog = WebElement(driver, '#submit')
        self.inputs_dialog = WebElement(driver, '.modal-dialog input')
        self.input_first_name = WebElement(driver, 'input#firstName')
        self.input_last_name = WebElement(driver, '#lastName')
        self.input_email = WebElement(driver, '#userEmail')
        self.input_age = WebElement(driver, '#age')
        self.input_salary = WebElement(driver, '#salary')
        self.input_department = WebElement(driver, '#department')
        self.added_row = WebElement(driver, '.rt-tr-group:nth-child(4)')
        self.row_first_name = WebElement(driver, '.rt-tr-group:nth-child(4)> div > div:nth-child(1)')
        self.row_last_name = WebElement(driver, '.rt-tr-group:nth-child(4)> div > div:nth-child(2)')
        self.row_age = WebElement(driver, '.rt-tr-group:nth-child(4)> div > div:nth-child(3)')
        self.row_email = WebElement(driver, '.rt-tr-group:nth-child(4)> div > div:nth-child(4)')
        self.row_salary = WebElement(driver, '.rt-tr-group:nth-child(4)> div > div:nth-child(5)')
        self.row_department = WebElement(driver, '.rt-tr-group:nth-child(4)> div > div:nth-child(6)')
        self.added_row_edit = WebElement(driver, '#edit-record-4')
        self.added_row_delete = WebElement(driver, '#delete-record-4')
        self.header_first_name = WebElement(driver, '.-cursor-pointer:nth-of-type(1)')
        self.header_last_name = WebElement(driver, '.-cursor-pointer:nth-of-type(2)')
        self.header_age = WebElement(driver, '.-cursor-pointer:nth-of-type(3)')
        self.header_email = WebElement(driver, '.-cursor-pointer:nth-of-type(4)')
        self.header_salary = WebElement(driver, '.-cursor-pointer:nth-of-type(5)')
        self.header_department = WebElement(driver, '.-cursor-pointer:nth-of-type(6)')

