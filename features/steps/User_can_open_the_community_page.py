from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open the main page')
def open_the_main_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@when('Log in to the page')
def log_in_to_the_page(context):
    email_field = context.driver.find_element(By.ID, 'email-2')
    password_field = context.driver.find_element(By.ID, 'field')
    login_button = context.driver.find_element(By.CSS_SELECTOR, '[class*="login-button"]')

    email_field.click()
    email_field.send_keys("Matthew.andre@yahoo.com")

    password_field.click()
    password_field.send_keys("123456789")

    login_button.click()


@when('Click on settings option')
def click_on_settings_option(context):
    context.driver.find_element(By.XPATH, "//div[contains(text(), 'Settings') and @class='menu-button-text']").click()


@when('Click on Community option')
def click_on_community_option(context):
    context.driver.find_element(By.XPATH, "//div[contains(text(), 'Community') and @class='setting-text']").click()


@then('Verify the Community page opens')
def verify_the_community_page_opens(context):
    context.driver.find_element(By.XPATH, "//div[@class='community-blog']")


@then('Verify at least two articles are available')
def verify_at_least_two_articles_are_available(context):
    articles = context.driver.find_elements(By.XPATH, "//div[@class='community-cards']")
    assert len(articles) >= 2, "Expected at least two articles, but found fewer."
