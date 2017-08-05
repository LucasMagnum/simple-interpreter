from behave import given, then, when


@given('I import the interpreter')
def import_interpreter(context):
    from interpreter import Interpreter
    from interpreter.lexer import Lexer
    from interpreter.parser import Parser
    context.interpreter = Interpreter
    context.lexer = Lexer
    context.parser = Parser


@when('I type "{text}" and execute')
def execute(context, text):
    lexer = context.lexer(text)
    parser = context.parser(lexer)
    interpreter = context.interpreter(parser)
    context.result = interpreter.interpret()


@then('I should see "{text}"')
def see_results(context, text):
    assert str(context.result) == text
