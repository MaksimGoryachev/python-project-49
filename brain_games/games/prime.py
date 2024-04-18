from random import randint


def right_answer_game():
    number = randint(2, 101)
    expression = f'{number}'
    right_answer = 'yes'
    for _ in range(2, number // 2 + 1):
        if number % _ == 0:
            right_answer = 'no'
            break
    return right_answer, expression
