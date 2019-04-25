from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class TestCRMLogin:
    """Tests for CRM login"""
    def test_successful_login_to_crm(self):
        """Successful admin login"""
        driver = Chrome()
        driver.get('https://demo.django-crm.io/login/')
        email_input = driver.find_element(By.ID, 'exampleInputEmail1')
        password_input = driver.find_element(By.ID, 'exampleInputPassword1')
        login_button = driver.find_element_by_class_name('btn-danger')

        email_input.send_keys('admin@micropyramid.com')
        password_input.send_keys('admin')
        login_button.submit()

        assert driver.find_element_by_id('contacts').is_displayed()
        sleep(2)
        driver.quit()

    def test_unsuccessful_login(self):
        """Test unsuccessful login"""
        # bla bla bla....
        pass
        