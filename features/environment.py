from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from support.logger import logger


def browser_init(context):
    """
    :param context: Behave context
    """

    service = Service(executable_path='/Users/matthewandre/Desktop/internship-project/chromedriver')
    context.driver = webdriver.Chrome(service=service)
    ### OTHER BROWSERS ###
    # service = Service(executable_path='/Users/matthewandre/Desktop/internship-project/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    #context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1200,800")
    # service = Service(executable_path='/Users/matthewandre/Desktop/internship-project/chromedriver')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # bs_user = 'matthewandre_5s6UmJ'
    # bs_key = 'fxpy9pi1xYELVssxbCzk'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "osVersion": "16",
    #     "deviceName": "iPhone 12 Pro",
    #     # 'os': 'Windows',
    #     # 'osVersion': '10',
    #     # 'browserName': "Firefox",
    #     'sessionName': 'Mobile test user can open the community page'
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # To run behave with allure in terminal, use:
    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/User_can_open_the_community_page.feature
    # To generate report, run:
    # allure serve test_results /

    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "Pixel 5"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
