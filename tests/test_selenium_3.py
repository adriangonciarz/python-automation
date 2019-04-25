import os

from pages.create_document_page import CreateDocumentPage
from pages.dashboard_page import DashboardPage
from pages.document_list_page import DocumentListPage
from pages.login_page import LoginPage
from utils import utils


class TestCRMLogin:
    """Tests for CRM login"""

    def test_successful_login_to_crm(self, driver):
        """Successful admin login"""
        login_page = LoginPage(driver)
        login_page.login('admin@micropyramid.com', 'admin')
        dashboard_page = DashboardPage(driver)
        dashboard_page.assert_top_right_drop_down_is_displayed()

    def test_unsuccessful_login(self, driver):
        """Test unsuccessful login"""
        login_page = LoginPage(driver)
        login_page.login('wrong', 'admin')
        login_page.assert_error_is_displayed()

    def test_create_new_document(self, driver):
        filepath = os.path.abspath('../files/myfile.txt')
        document_name = utils.randomize_string('doc_title')
        LoginPage(driver).login('admin@micropyramid.com', 'admin')
        DashboardPage(driver).go_to_documents()
        DocumentListPage(driver).click_create_new_document()
        CreateDocumentPage(driver).create_document(document_name, filepath)
