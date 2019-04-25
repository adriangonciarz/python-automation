from selenium.webdriver.common.by import By


class LoginPage:
    _email_input_selector = (By.ID, 'exampleInputEmail1')
    _password_input_selector = (By.ID, 'exampleInputPassword1')
    _login_button_selector = (By.CLASS_NAME, 'btn-danger')
    _login_error_selector = (By.CLASS_NAME, 'error')

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(*self._email_input_selector).send_keys(email)
        self.driver.find_element(*self._password_input_selector).send_keys(password)
        self.driver.find_element(*self._login_button_selector).submit()

    def assert_error_is_displayed(self):
        assert self.driver.find_element(*self._login_error_selector).is_displayed()
