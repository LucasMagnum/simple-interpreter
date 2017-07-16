from behave import given, then, when


@given('I import the interpreter')
def import_interpreter(context):
    from interpreter import Interpreter
    context.interpreter = Interpreter


@when('I type "{text}" and execute')
def execute(context, text):
    context.result = context.interpreter(text).execute()


@then('I should see "{text}"')
def see_results(context, text):
    assert str(context.result) == text
