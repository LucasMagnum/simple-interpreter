import pytest

from interpreter import Interpreter
from interpreter.tokens import INTEGER, PLUS, EOF


def test_error_should_raise_exception():
    """Error should raise exception."""
    interpreter = Interpreter(None)

    with pytest.raises(Exception):
        interpreter.error()


def test_execute_sum_to_numbers():
    """Execute should evalue the expression."""
    interpreter = Interpreter("2+3")
    assert interpreter.execute() == 5


def test_eat_change_current_token():
    """Eat should pass to a next token."""
    interpreter = Interpreter("2+3")
    interpreter.current_token = interpreter.get_next_token()

    assert interpreter.current_token.token_type == INTEGER

    interpreter.eat(INTEGER)

    assert interpreter.current_token.token_type == PLUS
    assert interpreter.current_token.value == "+"


def test_eat_raise_exception_on_fail():
    """Eat should raise exception on fail."""
    interpreter = Interpreter("2+3")
    interpreter.current_token = interpreter.get_next_token()

    assert interpreter.current_token.token_type == INTEGER

    with pytest.raises(Exception):
        interpreter.eat(PLUS)


def test_get_next_token_returns_eof():
    """Get next token should return EOF when tokens ends."""
    interpreter = Interpreter("")

    next_token = interpreter.get_next_token()

    assert next_token.token_type == EOF
    assert next_token.value is None


def test_get_next_token_returns_integer():
    """Get next token should convert digit to ints."""
    interpreter = Interpreter("1")

    next_token = interpreter.get_next_token()

    assert next_token.token_type == INTEGER
    assert next_token.value == 1


def test_get_next_token_returns_plus():
    """Get next token should convert plus signal to it token."""
    interpreter = Interpreter("+")

    next_token = interpreter.get_next_token()

    assert next_token.token_type == PLUS
    assert next_token.value == "+"


def test_get_next_token_should_raise_exception_on_fail():
    """When get next token fails should raise exception."""
    interpreter = Interpreter("-")

    with pytest.raises(Exception):
        interpreter.get_next_token()
