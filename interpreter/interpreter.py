import operator

from .tokens import Token, EOF, INTEGER, MINUS, PLUS


class Interpreter(object):

    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text.replace(" ", "") if text else text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def execute(self):
        """execute -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the current token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        self.eat([PLUS, MINUS])

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        operators = {
            PLUS: operator.add,
            MINUS: operator.sub
        }
        result = operators[op.token_type](left.value, right.value)
        return result

    def eat(self, token_types):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if not isinstance(token_types, (list, tuple)):
            token_types = [token_types]

        if self.current_token.token_type in token_types:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        while current_char.isdigit() and self.pos < len(text) - 1:
            next_char = text[self.pos + 1]

            if next_char.isdigit():
                current_char += next_char
                self.pos += 1
            else:
                break

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()

    def error(self):
        raise Exception('Error parsing input')
