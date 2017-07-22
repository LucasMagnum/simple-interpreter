"""Token representation."""

import operator


# token types
INTEGER = 'INTEGER'
operations = {
    '+': {'type': 'PLUS', 'func': operator.add},
    '-': {'type': 'MINUS', 'func': operator.sub},
    '*': {'type': 'MUL', 'func': operator.mul},
    '/': {'type': 'DIV', 'func': operator.truediv}
}


class Token(object):

    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value
        self.func = (operations[value]['func']
                     if value in operations
                     else None)

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


def parse_tokens(text):
    """Parse text and return next token."""
    token = ''

    clean_text = text.replace(" ", "")

    for pos, term in enumerate(clean_text):
        if term.isdigit():
            token += term
            if pos < len(clean_text) - 1:
                continue

        if token.isdigit():
            yield Token(INTEGER, int(token))
            token = ''

        operation = operations.get(term)

        if operation is not None:
            yield Token(operation['type'], term)
            continue

        if not term.isdigit() and term not in operations:
            raise Exception("Error while parsing tokens")

    raise StopIteration
