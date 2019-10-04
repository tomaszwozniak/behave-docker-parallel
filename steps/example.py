from behave import given, when, then
from time import sleep


@given("I am logged as {} user")
def step_impl(context, user):
    pass


@when("I create Staff user")
def step_impl(context):
    sleep(1)


@when('I change "Last name" to "Johnson"')
def step_impl(context):
    sleep(2)


@when('I click "Save and continue editing" button')
def step_impl(context):
    sleep(2)


@when("I remove Staff user")
def step_impl(context):
    sleep(2)


@then("Staff user is visible on user list page")
def step_impl(context):
    sleep(2)


@then("I should be able to login as Staff user")
def step_impl(context):
    sleep(2)


@then('I should see "Johnson" in "Last name" field')
def step_impl(context):
    sleep(2)


@then("Staff user is not visible on user list page")
def step_impl(context):
    sleep(2)


@when("I create new group")
def step_impl(context):
    sleep(5)


@then("Created group is visible on the list")
def step_impl(context):
    sleep(1)


@when('I add permission "can add user"')
def step_impl(context):
    sleep(3)


@then('I should see "can add user" in "Choosen permissions"')
def step_impl(context):
    sleep(1)


@when("I remove previously created group")
def step_impl(context):
    sleep(3)


@then("Group is not visible on the list")
def step_impl(context):
    sleep(1)
    assert False, "something went wrong"
