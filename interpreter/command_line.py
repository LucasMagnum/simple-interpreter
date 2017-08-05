from .interpreter import Interpreter
from .lexer import Lexer
from .parser import Parser


def main():

    while True:
        try:
            text = input('simple-interpreter> ')
        except EOFError:
            break

        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
