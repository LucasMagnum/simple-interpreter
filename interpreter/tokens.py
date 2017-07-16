"""Token representation."""

# token types
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'


class Token(object):
    def __init__(self, token_type, value):
        # token type: INTEGER, PLUS, or EOF
        self.token_type = token_type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({token_type}, {value})'.format(
            token_type=self.token_type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()
