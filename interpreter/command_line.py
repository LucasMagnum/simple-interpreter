from .interpreter import Interpreter
from .lexer import Lexer


def main():

    while True:
        try:
            text = input('simple-interpreter> ')
        except EOFError:
            break

        if not text:
            continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
