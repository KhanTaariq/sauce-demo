import time

from behave import given, when, then

from pageobjects.performance_glitch_user import Performance_GlitchPageObject


@given('The Login page is open (performance)')
def step_impl(context):
    context.current_page = Performance_GlitchPageObject()
    context.current_page.open()
    time.sleep(1.5)


@when('the user enters the username"performance_glitch_user"')
def step_impl(context):
    context.current_page = Performance_GlitchPageObject()

    context.current_page = context.current_page.name()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_name()
    time.sleep(1.5)

@then('enter the password "secret_sauce"')
def step_impl(context):
    context.current_page = Performance_GlitchPageObject()
    context.current_page = context.current_page.passwordd()
    time.sleep(1.5)
    context.current_page = context.current_page.enter_p_word()
    time.sleep(1.5)


@then('the user logs in')
def step_impl(context):
    context.current_page = Performance_GlitchPageObject()
    context.current_page = context.current_page.button()
    time.sleep(1.5)


@then('it takes the user to the next page "{title}"')
def step_impl(context, title):
    context.current_page = Performance_GlitchPageObject()
    assert title in context.current_page.performance_title_products()
    # context.current_page = context.current_page.performance_title_products()
    time.sleep(1.5)