from selenium.webdriver.common.by import By
from pages.base_page import Page


class SettingsPage(Page):
    # Locators specific to the settings page
    SETTINGS_OPTION = (By.XPATH, "//div[contains(text(), 'Settings') and @class='menu-button-text']")

    def click_settings_option(self):
        self.wait_for_element_clickable(*self.SETTINGS_OPTION)
        self.click(*self.SETTINGS_OPTION)
