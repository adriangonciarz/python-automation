from selenium.webdriver.common.by import By


class DashboardPage:
    _contacts_top_button_selector = (By.ID, 'contacts')
    _leads_top_button_selector = (By.ID, 'leads')
    _top_right_drop_down_selector = (By.CLASS_NAME, 'abcd')

    def __init__(self, driver):
        self.driver = driver

    def assert_top_right_drop_down_is_displayed(self):
        assert self.driver.find_element(*self._top_right_drop_down_selector).is_displayed()
