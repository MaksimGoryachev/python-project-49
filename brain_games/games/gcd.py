from random import randint


def returns_right_answer_round():
    number_1 = randint(1, 50)
    number_2 = randint(1, 50)
    expression = f'{number_1} {number_2}'
    for _ in range(max(number_1 // 2, number_2 // 2), 0, -1):
        if number_1 % _ == 0 and number_2 % _ == 0:
            right_answer = _
            break
    return expression, right_answer


def generate_data_for_game():
    question = 'Find the greatest common divisor of given numbers.'
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        expression, right_answer = returns_right_answer_round()
        expressions.append(expression)
        right_answers.append(right_answer)
    return question, right_answers, expressions
