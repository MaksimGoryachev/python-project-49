from random import randint


def is_even(num: int) -> bool:
    return num % 2 == 0


def returns_right_answer_round():
    number = randint(1, 1000)
    expression = f'{number}'
    right_answer = 'yes' if is_even(number) else 'no'
    return expression, right_answer


def generate_data_for_game():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        expression, right_answer = returns_right_answer_round()
        expressions.append(expression)
        right_answers.append(right_answer)
    return question, right_answers, expressions
