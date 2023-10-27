from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on menu option')
def click_on_settings_option(context):
    context.driver.find_element(By.XPATH, "//div[@class='mobile-top-menu']").click()


@then('Verify at least one article is available')
def verify_at_least_one_article_is_available(context):
    articles = context.driver.find_elements(By.XPATH, "//div[@class='community-cards']")
    assert len(articles) >= 1, "Expected at least one article, but found fewer."
