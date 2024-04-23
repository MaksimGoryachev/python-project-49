from random import randint, choice


def right_answer_game():
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        number_1 = randint(1, 50)
        number_2 = randint(1, 50)
        operation = choice(['+', '-', '*'])
        expression = f'{number_1} {operation} {number_2}'
        if operation == '+':
            right_answer = number_1 + number_2
        elif operation == '-':
            right_answer = number_1 - number_2
        else:
            right_answer = number_1 * number_2
        expressions.append(expression)
        right_answers.append(right_answer)
    return right_answers, expressions
