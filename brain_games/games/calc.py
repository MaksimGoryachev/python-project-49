from random import randrange, choice


QUESTION = 'What is the result of the expression?'

NUMBER_1_MAX = 50
NUMBER_2_MAX = 50


def calculate(num_1, num_2, operation) -> int:

    if operation == '+':
        right_answer = num_1 + num_2
    elif operation == '-':
        right_answer = num_1 - num_2
    else:
        right_answer = num_1 * num_2

    return right_answer


def generate_data_for_game() -> tuple:

    number_1 = randrange(NUMBER_1_MAX)
    number_2 = randrange(NUMBER_2_MAX)

    operation = choice(['+', '-', '*'])

    expression = f'{number_1} {operation} {number_2}'
    right_answer = calculate(number_1, number_2, operation)

    return right_answer, expression
