from interpreter import Interpreter


def test_execute_returns_integer():
    """Execute should return only one integer when is given."""
    interpreter = Interpreter("1")
    assert interpreter.execute() == 1


def test_execute_sum_two_numbers():
    """Execute should evaluate the expression."""
    interpreter = Interpreter("2+3")
    assert interpreter.execute() == 5


def test_execute_sum_two_numbers_with_space_betwen_them():
    """Execute should evaluate the expression correctly."""
    interpreter = Interpreter("12 + 50")
    assert interpreter.execute() == 62


def test_execute_subtracts_two_numbers_with_space_betwen_them():
    """Execute should evaluate the expression correctly."""
    interpreter = Interpreter("12 - 12")
    assert interpreter.execute() == 0


def test_execute_multiply_two_numbers_with_space_betwen_them():
    """Execute should evaluate the expression correctly."""
    interpreter = Interpreter("10 * 10")
    assert interpreter.execute() == 100


def test_execute_divide_two_numbers_with_space_betwen_them():
    """Execute should evaluate the expression correctly."""
    interpreter = Interpreter("100 / 10")
    assert interpreter.execute() == 10
