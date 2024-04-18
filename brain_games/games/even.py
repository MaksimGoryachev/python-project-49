from random import randint


def right_answer_game():
    number_1 = randint(1, 1000)
    expression = f'{number_1}'
    if number_1 % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, expression
