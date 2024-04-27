from random import randint, choice


def returns_right_answer_round(num_1, num_2, operation) -> int:
    if operation == '+':
        right_answer = num_1 + num_2
    elif operation == '-':
        right_answer = num_1 - num_2
    else:
        right_answer = num_1 * num_2
    return right_answer


def generate_data_for_game() -> tuple:
    number_1 = randint(1, 50)
    number_2 = randint(1, 50)
    operation = choice(['+', '-', '*'])
    expression = f'{number_1} {operation} {number_2}'
    right_answer = returns_right_answer_round(number_1, number_2, operation)
    return right_answer, expression


question = 'What is the result of the expression?'
