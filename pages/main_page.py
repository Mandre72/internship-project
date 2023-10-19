from time import sleep
from pages.base_page import Page


class MainPage(Page):

    def open_main_page(self):
        self.driver.get('https://soft.reelly.io/sign-in')
        self.driver.get('https://soft.reelly.io/sign-in')
        sleep(2)
        self.driver.refresh()

