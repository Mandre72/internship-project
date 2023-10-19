from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    # Locators specific to the login page
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class*="login-button"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://soft.reelly.io/sign-in')

    def login(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BUTTON)


