# -*- coding: utf-8 -*-
# flake8: noqa
from behave import given, then, when


@given("I am logged as {} user")
def step_impl(context, user):
    pass


@when("I create Staff user")
def step_impl(context):
    pass


@when('I change "Last name" to "Johnson"')
def step_impl(context):
    pass


@when('I click "Save and continue editing" button')
def step_impl(context):
    pass


@when("I remove Staff user")
def step_impl(context):
    pass


@then("Staff user is visible on user list page")
def step_impl(context):
    pass


@then("I should be able to login as Staff user")
def step_impl(context):
    pass


@then('I should see "Johnson" in "Last name" field')
def step_impl(context):
    pass


@then("Staff user is not visible on user list page")
def step_impl(context):
    pass


@when("I create new group")
def step_impl(context):
    pass


@then("Created group is visible on the list")
def step_impl(context):
    pass


@when('I add permission "can add user"')
def step_impl(context):
    pass


@then('I should see "can add user" in "Choosen permissions"')
def step_impl(context):
    pass


@when("I remove previously created group")
def step_impl(context):
    pass


@then("Group is not visible on the list")
def step_impl(context):
    assert False, "something went wrong"
