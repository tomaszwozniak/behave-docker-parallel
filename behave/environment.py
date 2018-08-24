from selenium.webdriver.remote import webdriver

WEBDRIVER_URL = 'http://selenium-hub:4444/wd/hub'

DEFAULT_BROWSER = 'firefox'

DESIRED_CAPABILITIES = {
    'platform': 'ANY',
    'browserName': DEFAULT_BROWSER,
    'version': '',
    'javascriptEnabled': True
}


def before_all(context):
    context.browser = webdriver.WebDriver(
        WEBDRIVER_URL,
        desired_capabilities=DESIRED_CAPABILITIES
    )


def after_all(context):
    context.browser.quit()
