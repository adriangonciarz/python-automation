from selenium.webdriver.common.by import By


class DocumentListPage:
    _create_new_document_selector = (By.PARTIAL_LINK_TEXT, 'Add New Document')

    def __init__(self, driver):
        self.driver = driver

    def click_create_new_document(self):
        self.driver.find_element(*self._create_new_document_selector).click()