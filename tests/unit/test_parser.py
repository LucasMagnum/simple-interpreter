import pytest

from interpreter.ast import Num, BinOp, UnaryOp
from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.tokens import (
    Token, INTEGER_CONST, PLUS, MINUS, MUL, FLOAT_DIV
)


def test_error():
    """Should raise exception."""
    parser = Parser(Lexer("1 1"))

    with pytest.raises(Exception):
        parser.error()


def test_eat_trown_an_error():
    """Should raise exception."""
    parser = Parser(Lexer("1"))

    with pytest.raises(Exception):
        parser.eat("MUL")


def test_expr_returns_a_num_node():
    """Expr should return only num node when it's given."""
    parser = Parser(Lexer("1"))

    node = parser.expr()

    assert isinstance(node, Num)
    assert node.token == Token(INTEGER_CONST, 1)


def test_expr_returns_a_unary_node():
    """Expr should return only num node when it's given."""
    parser = Parser(Lexer("-1"))

    node = parser.expr()

    assert isinstance(node, UnaryOp)
    assert node.token == Token(MINUS, "-")
    assert node.expr.token == Token(INTEGER_CONST, 1)


def test_expr_sum_two_numbers():
    """Expr should return a BinOp."""
    parser = Parser(Lexer("2 + 3"))

    node = parser.expr()

    assert isinstance(node, BinOp)
    assert isinstance(node.left, Num)
    assert isinstance(node.right, Num)

    assert node.left.token == Token(INTEGER_CONST, 2)
    assert node.op == Token(PLUS, "+")
    assert node.right.token == Token(INTEGER_CONST, 3)


def test_expr_parse_two_numbers_with_space_betwen_them():
    """
    Expr should evaluate the expression correctly.

    >> 12 - 11 - 0
    BinOp(BinOp(12 - 11) - 0)
    """
    parser = Parser(Lexer("12 - 11 - 0"))

    node = parser.expr()

    assert isinstance(node, BinOp)
    assert isinstance(node.left, BinOp)
    assert isinstance(node.right, Num)

    left_op = node.left
    assert left_op.left.token == Token(INTEGER_CONST, 12)
    assert left_op.op == Token(MINUS, "-")
    assert left_op.right.token == Token(INTEGER_CONST, 11)

    right_op = node.right
    assert right_op.token == Token(INTEGER_CONST, 0)


def test_expr_multiply():
    """Expr should evaluate the expression correctly.

    >> 10 * 5 * 2
    BinOp(BinOp(10 * 5) * 2)

    """
    parser = Parser(Lexer("10 * 5 * 2 "))

    node = parser.expr()

    assert isinstance(node, BinOp)
    assert isinstance(node.left, BinOp)
    assert isinstance(node.right, Num)

    left_op = node.left
    assert left_op.left.token == Token(INTEGER_CONST, 10)
    assert left_op.op == Token(MUL, "*")
    assert left_op.right.token == Token(INTEGER_CONST, 5)

    right_op = node.right
    assert right_op.token == Token(INTEGER_CONST, 2)


def test_expr_sum_with_precedence():
    """
    Expr should evaluate the expression correctly.

    >> 1 + 2 * 3
    BinOp(1 + BinOp(2 * 3))

    """
    parser = Parser(Lexer("1 + 2 * 3"))
    node = parser.expr()

    assert isinstance(node, BinOp)
    assert isinstance(node.left, Num)
    assert isinstance(node.right, BinOp)

    left_op = node.left
    assert left_op.token == Token(INTEGER_CONST, 1)

    assert node.op == Token(PLUS, "+")

    right_op = node.right
    assert right_op.left.token == Token(INTEGER_CONST, 2)
    assert right_op.op == Token(MUL, "*")
    assert right_op.right.token == Token(INTEGER_CONST, 3)


def test_expr_divide_two_numbers_with_space_betwen_them():
    """Expr should evaluate the expression correctly."""
    parser = Parser(Lexer("100 / 10"))

    node = parser.expr()

    assert isinstance(node, BinOp)
    assert isinstance(node.left, Num)
    assert isinstance(node.right, Num)

    assert node.left.token == Token(INTEGER_CONST, 100)
    assert node.op == Token(FLOAT_DIV, "/")
    assert node.right.token == Token(INTEGER_CONST, 10)


def test_expr_with_nested_operations():
    """Expr should handle nested operations.

    >> 10 * (2 + 5)
    BinOp(10 * BinOp(2 + 5))

    """
    parser = Parser(Lexer("10 * (2 + 5)"))
    node = parser.expr()

    assert isinstance(node, BinOp)
    assert isinstance(node.left, Num)
    assert isinstance(node.right, BinOp)

    left_op = node.left
    assert left_op.token == Token(INTEGER_CONST, 10)

    assert node.op == Token(MUL, "*")

    right_op = node.right
    assert right_op.left.token == Token(INTEGER_CONST, 2)
    assert right_op.op == Token(PLUS, "+")
    assert right_op.right.token == Token(INTEGER_CONST, 5)
