import time

from behave import given, when, then

from pageobjects.problem_user import Problem_UserPageObject


@given('The Login page is open (problem user)')
def step_impl(context):
    context.current_page = Problem_UserPageObject()
    context.current_page.open()
    time.sleep(1.5)


@when('the user enters the username"problem_user"')
def step_impl(context):
    context.current_page = Problem_UserPageObject()

    context.current_page = context.current_page.name()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_name()
    time.sleep(1.5)

@then('password "secret_sauce" is used')
def step_impl(context):
    context.current_page = Problem_UserPageObject()
    context.current_page = context.current_page.passwordd()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_p_word()
    time.sleep(1.5)


@then('the user clicks the login button that is displayed')
def step_impl(context):
    context.current_page = Problem_UserPageObject()
    context.current_page = context.current_page.button()
    time.sleep(1.5)


@then('it takes the user to the products page that displays the cute puppies')
def step_impl(context):
    context.current_page = Problem_UserPageObject()
    context.current_page = context.current_page.problem_user_title_products()
    time.sleep(1.5)