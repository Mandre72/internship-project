# from pages.signin_page import SignInPage
# from pages.settings_page import SettingsPage
# from pages.community_page import CommunityPage
# from behave import given, when, then
#
#
# @given('Open the main page')
# def open_the_main_page(context):
#     context.driver.get('https://soft.reelly.io/sign-in')
#
#
# @when('Login to the page')
# def login_to_the_page(context):
#     sign_in_page = SignInPage(context.driver)
#     sign_in_page.login("Matthew.andre@yahoo.com", "123456789")
#
#
# @when('Click on settings option')
# def click_on_settings_option(context):
#     settings_page = SettingsPage(context.driver)
#     settings_page.click_settings_option()
#
#
# @when('Click on Community option')
# def click_community_option(context):
#     community_page = CommunityPage(context.driver)
#     community_page.click_community_option()
#
#
# @then('Verify the Community page opens')
# def verify_community_page_opens(context):
#     community_page = CommunityPage(context.driver)
#     community_page.verify_community_page_opens()
#
#
# @then('Verify at least two articles are available')
# def verify_at_least_two_articles_available(context):
#     community_page = CommunityPage(context.driver)
#     community_page.verify_at_least_two_articles_available()
