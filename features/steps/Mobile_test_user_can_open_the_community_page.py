import time
from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on menu option')
def click_on_settings_option(context):
    context.driver.find_element(By.XPATH, "//div[@class='mobile-top-menu']").click()


@then('Verify two articles are available')
def verify_two_articles_are_available(context):
    time.sleep(2)
    articles = context.driver.find_elements(By.XPATH, "//div[@class='community-cards']")
    assert len(articles) >= 2, "Expected at least two articles, but found fewer."
    print(len(articles))
    #My test passes and fails it is not stable