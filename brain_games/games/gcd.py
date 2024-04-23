from random import randint


def right_answer_game():
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        number_1 = randint(1, 50)
        number_2 = randint(1, 50)
        expression = f'{number_1} {number_2}'
        for _ in range(max(number_1 // 2, number_2 // 2), 0, -1):
            if number_1 % _ == 0 and number_2 % _ == 0:
                right_answer = _
                break
        expressions.append(expression)
        right_answers.append(right_answer)
    return right_answers, expressions
