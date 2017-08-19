"""Token representation."""

INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF'
)

ID, ASSIGN, BEGIN, END, SEMI, DOT = (
    'ID', 'ASSIGN', 'BEGIN', 'END', 'SEMI', 'DOT'
)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __eq__(self, token):
        return self.type == token.type and self.value == token.value

    def __repr__(self):
        return self.__str__()
