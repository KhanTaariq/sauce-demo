import time

from behave import given, when, then

from pageobjects.standard_user import standard_loginPageObject


@given('The Login page is open')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page.open()
    time.sleep(1.5)


@when('the user enters the username "standard_user"')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page = context.current_page.name()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_name()
    time.sleep(1.5)

@then('password "secret_sauce"')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page = context.current_page.passwordd()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_passwrd()
    time.sleep(1.5)


@then('the user clicks the login button')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page = context.current_page.button()
    time.sleep(1.5)


@then('it takes the user to the products page')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page = context.current_page.the_title()
    time.sleep(1.5)


@given('The Login page is open a second time')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page.open()
    time.sleep(1.5)


@when('the user enters the username "standard_user" a second time')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page = context.current_page.name()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_name()
    time.sleep(1.5)

@then('password "incorrect"')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page = context.current_page.passwordd()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_incorrect_passwrd()
    time.sleep(1.5)


@then('the user clicks the login button a second time')
def step_impl(context):
    context.current_page = standard_loginPageObject()
    context.current_page = context.current_page.button()
    time.sleep(1.5)


@then('the user get the error message "{error_message_displayed}"')
def step_impl(context, error_message_displayed):
    context.current_page = standard_loginPageObject()
    assert error_message_displayed in context.current_page.standard_user_message_error()
    time.sleep(1.5)

