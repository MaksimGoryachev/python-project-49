from random import randint


def right_answer_game():
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        number = randint(2, 101)
        expression = f'{number}'
        right_answer = 'yes'
        for _ in range(2, number // 2 + 1):
            if number % _ == 0:
                right_answer = 'no'
                break
        expressions.append(expression)
        right_answers.append(right_answer)
    return right_answers, expressions
