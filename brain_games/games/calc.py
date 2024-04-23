from random import randint, choice


def returns_right_answer_round():
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
    return expression, right_answer


def generate_data_for_game():
    question = 'What is the result of the expression?'
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        expression, right_answer = returns_right_answer_round()
        expressions.append(expression)
        right_answers.append(right_answer)
    return question, right_answers, expressions
