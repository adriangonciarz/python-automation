from selenium.webdriver.common.by import By


class CreateDocumentPage:
    _document_title_selector = (By.ID, 'title')
    _document_file_selector = (By.ID, 'document_file')
    _save_button_selector = (By.ID, 'submit_btn')

    def __init__(self, driver):
        self.driver = driver

    def create_document(self, title, filepath):
        self.driver.find_element(*self._document_title_selector).send_keys(title)
        self.driver.find_element(*self._document_file_selector).send_keys(filepath)
        self.driver.find_element(*self._save_button_selector).submit()