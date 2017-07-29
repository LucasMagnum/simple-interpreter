from behave import given, then, when


@given('I import the interpreter')
def import_interpreter(context):
    from interpreter import Interpreter
    from interpreter.lexer import Lexer
    context.interpreter = Interpreter
    context.lexer = Lexer


@when('I type "{text}" and execute')
def execute(context, text):
    lexer = context.lexer(text)
    context.result = context.interpreter(lexer).expr()


@then('I should see "{text}"')
def see_results(context, text):
    assert str(context.result) == text
