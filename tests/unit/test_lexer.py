import pytest

from interpreter.lexer import Lexer


def test_lexer_not_found_token():
    lexer = Lexer("$")

    with pytest.raises(Exception):
        lexer.get_next_token()
