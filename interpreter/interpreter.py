
from .tokens import parse_tokens


class Interpreter(object):

    def __init__(self, text):
        self.text = text

    def execute(self):
        """Get the tokens and evaluate the result."""
        result = 0
        op = None

        for token in parse_tokens(self.text):
            if token.func:
                op = token.func
                continue

            if op:
                result = op(result, token.value)
                continue

            result = token.value

        return result
