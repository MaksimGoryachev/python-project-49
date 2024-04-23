from random import randint


def returns_right_answer_round():
    number = randint(2, 101)
    expression = f'{number}'
    right_answer = 'yes'
    for _ in range(2, number // 2 + 1):
        if number % _ == 0:
            right_answer = 'no'
            break
    return expression, right_answer


def generate_data_for_game():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        expression, right_answer = returns_right_answer_round()
        expressions.append(expression)
        right_answers.append(right_answer)
    return question, right_answers, expressions
