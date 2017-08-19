import pytest

from interpreter.ast import Num
from interpreter.interpreter import Interpreter, NodeVisitor
from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.tokens import Token, INTEGER


class TestNodeVisitor(object):
    num_token = Num(Token(INTEGER, 1))

    def test_generic_visit_raise_exception(self):
        node = NodeVisitor()

        with pytest.raises(Exception):
            node.generic_visit(self.num_token)

    def test_visit_raise_exception_when_visit_not_found(self):
        node = NodeVisitor()

        with pytest.raises(Exception):
            node.visit(self.num_token)


class TestInterpreter(object):

    def test_interpreter_raises_exception_with_invalid_syntax(self):
        with pytest.raises(Exception):
            assert interpret("2 + 3") == 5

    def test_interpreter_with_empty_statement(self):
        assert interpret("BEGIN END.") is None


def interpret(expression):
    """Interpret expression and return the result."""
    lexer = Lexer(expression)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    return interpreter.interpret()
