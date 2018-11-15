# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

HUB_URL = os.environ.get("HUB_URL", "http://selenium-hub:4444/wd/hub")
BROWSER = os.environ.get("BROWSER", "firefox")
DESIRED_CAPABILITIES = {
    "platform": "ANY",
    "browserName": BROWSER,
    "version": "",
    "javascriptEnabled": True,
}


def before_all(context):

    browser = DESIRED_CAPABILITIES["browserName"].lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1600x2200")
        options.add_argument("--start-maximized")
        options.add_argument("--whitelisted-ips=")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
    elif browser == "firefox":
        options = FirefoxOptions()
        # see comment in docker-compose.yml re: bug in geckodriver
        # options.add_argument("--headless")
        # options.add_argument("--window-size 1600,2200")
        options.add_argument("--width=1600")
        options.add_argument("--height=2200")
        options.add_argument("--safe-mode")
    else:
        raise Exception(f"{browser} is not supported try: Chrome or Firefox")

    context.browser = webdriver.Remote(
        command_executor=HUB_URL,
        desired_capabilities=DESIRED_CAPABILITIES,
        options=options,
    )


def after_all(context):
    context.browser.quit()
