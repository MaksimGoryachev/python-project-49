from random import randint


def right_answer_game():
    right_answers = []
    expressions = []
    for _ in range(3):
        number_1 = randint(1, 1000)
        expression = f'{number_1}'
        if number_1 % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        expressions.append(expression)
        right_answers.append(right_answer)
    return right_answers, expressions
