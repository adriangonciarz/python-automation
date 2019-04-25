from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


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
