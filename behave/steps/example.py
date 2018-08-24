from behave import given, when, then
from time import sleep


@given('I am logged as Super user')
def step_impl(context):
    pass


@when('I create Stuff user')
def step_impl(context):
    sleep(1)


@when('I change "Last name" to "Johnson"')
def step_impl(context):
    sleep(2)


@when('I click "Save and continue editing" button')
def step_impl(context):
    sleep(2)


@when('I remove Stuff user')
def step_impl(context):
    sleep(2)


@then('Stuff user is visible on user list page')
def step_impl(context):
    sleep(2)


@then('I should be able to login as stuff user')
def step_impl(context):
    sleep(2)


@then('I should see "Johnson" in "Last name" field')
def step_impl(context):
    sleep(2)


@then('Stuff user is not visible on user list page')
def step_impl(context):
    sleep(2)


@when('I create new group')
def step_impl(context):
    sleep(5)


@then('Created group is visible on the list')
def step_impl(context):
    sleep(1)


@when('I add permission "can add user"')
def step_impl(context):
    sleep(3)


@then('I should see "can add user" in "Choosen permissions"')
def step_impl(context):
    sleep(1)


@when('I remove previously created group')
def step_impl(context):
    sleep(3)


@then('Group is not visible on the list')
def step_impl(context):
    sleep(1)
