from random import randint


def right_answer_game():
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        number_1 = randint(1, 1000)
        expression = f'{number_1}'
        if number_1 % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        expressions.append(expression)
        right_answers.append(right_answer)
    return right_answers, expressions
