import time

from behave import given, when, then

from pageobjects.locked_out_user import locked_outPageObject


@given('sourcedemo login page is open')
def step_impl(context):
    context.current_page = locked_outPageObject()
    context.current_page.open()
    time.sleep(1.5)


@when('the user inputs the username "locked_out_user"')
def step_impl(context):
    context.current_page = locked_outPageObject()

    context.current_page = context.current_page.name()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_name()
    time.sleep(1.5)

@then('for password "secret_sauce" is entered')
def step_impl(context):
    context.current_page = locked_outPageObject()
    context.current_page = context.current_page.passwordd()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_passwrd()
    time.sleep(1.5)


@then('the login button is clicked')
def step_impl(context):
    context.current_page = locked_outPageObject()
    context.current_page = context.current_page.button()
    time.sleep(1.5)


@then('displays error message for locked out user "{locked_out_user_error}"')
def step_impl(context, locked_out_user_error):
    context.current_page = locked_outPageObject()
    assert locked_out_user_error in context.current_page.locked_out_message_error()