from interpreter.tokens import Token


def test_token_has_type_and_value():
    """Token should have a type and value."""
    token = Token("INTEGER", 5)

    assert token.type == "INTEGER"
    assert token.value == 5


def test_token_str():
    token = Token("INTEGER", 5)
    assert str(token) == 'Token(INTEGER, 5)'


def test_token_repr():
    token = Token("INTEGER", 5)
    assert token.__repr__() == token.__str__()
