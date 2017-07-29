import pytest

from interpreter import Interpreter
from interpreter.lexer import Lexer


def test_error():
    """Should raise exception."""
    interpreter = Interpreter(Lexer("1 1"))

    with pytest.raises(Exception):
        interpreter.error()


def test_eat_trown_an_error():
    """Should raise exception."""
    interpreter = Interpreter(Lexer("1"))

    with pytest.raises(Exception):
        interpreter.eat("MUL")


def test_expr_returns_integer():
    """Expr should return only one integer when is given."""
    interpreter = Interpreter(Lexer("1"))
    assert interpreter.expr() == 1


def test_expr_sum_two_numbers():
    """Expr should evaluate the expression."""
    interpreter = Interpreter(Lexer("2+3"))
    assert interpreter.expr() == 5


def test_expr_sum_two_numbers_with_space_betwen_them():
    """Expr should evaluate the expression correctly."""
    interpreter = Interpreter(Lexer("12 + 50"))
    assert interpreter.expr() == 62


def test_expr_subtracts_two_numbers_with_space_betwen_them():
    """Expr should evaluate the expression correctly."""
    interpreter = Interpreter(Lexer("12 - 12 - 0"))
    assert interpreter.expr() == 0


def test_expr_multiply_two_numbers_with_space_betwen_them():
    """Expr should evaluate the expression correctly."""
    interpreter = Interpreter(Lexer("10 + 10 * 10 "))
    assert interpreter.expr() == 110


def test_expr_divide_two_numbers_with_space_betwen_them():
    """Expr should evaluate the expression correctly."""
    interpreter = Interpreter(Lexer("100 / 10 * 1"))
    assert interpreter.expr() == 10
