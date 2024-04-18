from random import randint


def right_answer_game():
    number_1 = randint(1, 50)
    number_2 = randint(1, 50)
    expression = f'{number_1} {number_2}'
    for _ in range(max(number_1//2, number_2//2), 0, -1):
        if number_1 % _ == 0 and number_2 % _ == 0:
            right_answer = _
            break
    return right_answer, expression
