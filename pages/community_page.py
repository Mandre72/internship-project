from selenium.webdriver.common.by import By
from pages.base_page import Page


class CommunityPage(Page):

    COMMUNITY_OPTION = (By.XPATH, "//div[contains(text(), 'Community') and @class='setting-text']")
    COMMUNITY_PAGE = (By.XPATH, "//div[@class='community-blog']")
    ARTICLES = (By.XPATH, "//div[@class='community-cards']")

    def click_community_option(self):
        self.click(*self.COMMUNITY_OPTION)

    def verify_community_page_opens(self):
        self.wait_for_element_clickable(self.COMMUNITY_PAGE)

    def verify_at_least_two_articles_available(self):
        articles = self.find_elements(*self.ARTICLES)
        assert len(articles) >= 2, "Expected at least two articles, but found fewer."
