from selenium.webdriver.common.by import By

class TestCRMLogin:
    """Tests for CRM login"""

    def test_successful_login_to_crm(self, driver):
        """Successful admin login"""
        driver.get('https://demo.django-crm.io/login/')
        self._login(driver, 'admin@micropyramid.com', 'admin')
        assert driver.find_element_by_id('contacts').is_displayed()
        driver.quit()

    def test_unsuccessful_login(self, driver):
        """Test unsuccessful login"""
        driver.get('https://demo.django-crm.io/login/')
        self._login(driver, 'wrong', 'admin')
        assert driver.find_element_by_class_name('error').is_displayed()
        driver.quit()

    def _login(self, driver, email, password):
        email_input = driver.find_element(By.ID, 'exampleInputEmail1')
        password_input = driver.find_element(By.ID, 'exampleInputPassword1')
        login_button = driver.find_element_by_class_name('btn-danger')

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.submit()