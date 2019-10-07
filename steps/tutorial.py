# -*- coding: utf-8 -*-
# flake8: noqa
import allure
from behave import given, then, when
from behave.runner import Context


@given("we have behave installed")
def step_impl(context):
    pass


@when("we implement a test")
def step_impl(context):
    assert True is not False


@then("selenium works!")
def step_impl(context: Context):
    context.browser.get("https://google.com")
    screenshot = context.browser.get_screenshot_as_png()
    allure.attach(
        "selenium works!",
        name="attachment",
        attachment_type=allure.attachment_type.TEXT,
    )
    allure.attach(
        screenshot, name="screenshot.png", attachment_type=allure.attachment_type.PNG
    )
