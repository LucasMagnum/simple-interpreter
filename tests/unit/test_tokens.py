import pytest

from interpreter.tokens import Token, parse_tokens


def test_token_has_type_and_value():
    """Token should have a type and value."""
    token = Token("INTEGER", 5)

    assert token.token_type == "INTEGER"
    assert token.value == 5


def test_token_str():
    token = Token("INTEGER", 5)
    assert str(token) == 'Token(INTEGER, 5)'


def test_token_repr():
    token = Token("INTEGER", 5)
    assert token.__repr__() == token.__str__()


def test_parse_tokens_raises_stop_iteration():
    """Parser should raise stop iteration when parsing is over."""
    tokens = parse_tokens("")

    with pytest.raises(StopIteration):
        next(tokens)


def test_parse_tokens_returns_integer():
    """Get next token should convert digit to ints."""
    tokens = parse_tokens("1")
    next_token = next(tokens)

    assert next_token.token_type == "INTEGER"
    assert next_token.value == 1


def test_parse_tokens_returns_plus():
    """Get next token should convert plus signal to it token."""
    tokens = parse_tokens("+")
    next_token = next(tokens)

    assert next_token.token_type == "PLUS"
    assert next_token.value == "+"


def test_parse_tokens_recognizes_minus():
    """Get next token should convert minus signal to it token."""
    tokens = parse_tokens("-")
    next_token = next(tokens)

    assert next_token.token_type == "MINUS"
    assert next_token.value == "-"


def test_parse_tokens_recognizes_mul():
    """Get next token should convert mult signal to it token."""
    tokens = parse_tokens("*")
    next_token = next(tokens)

    assert next_token.token_type == "MUL"
    assert next_token.value == "*"


def test_parse_tokens_recognizes_div():
    """Get next token should convert div signal to it token."""
    tokens = parse_tokens("/")
    next_token = next(tokens)

    assert next_token.token_type == "DIV"
    assert next_token.value == "/"


def test_parse_tokens_should_raise_exception_on_fail():
    """When get next token fails should raise exception."""
    tokens = parse_tokens("$")

    with pytest.raises(Exception):
        next(tokens)
