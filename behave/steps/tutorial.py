from behave import given, when, then
from time import sleep

@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('selenium works!')
def step_impl(context):
    sleep(10)
    context.browser.get('http://google.com')
