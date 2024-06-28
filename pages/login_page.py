import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasePageLocators

class LoginPage(BasePage):
    def register_new_user(self, email=None, password=None):
        if email is None:
            email = str(time.time()) + "@fakemail.org"
        if password is None:
            password = "default_password"  # Можно задать дефолтный пароль или генерировать случайным образом
        email_input = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-email')
        password_input1 = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password1')
        password_input2 = self.browser.find_element(By.CSS_SELECTOR, '#id_registration-password2')
        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        submit_button = self.browser.find_element(By.NAME, 'registration_submit')
        submit_button.click()
