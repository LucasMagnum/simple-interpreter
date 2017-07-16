from .interpreter import Interpreter


def main():

    while True:
        try:
            text = input('simple-interpreter> ')
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.execute()
        print(result)


if __name__ == '__main__':
    main()
