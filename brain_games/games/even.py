from random import randint


def is_even(num: int) -> bool:
    return num % 2 == 0


def returns_right_answer_round(num):
    return 'yes' if is_even(num) else 'no'


def generate_data_for_game():
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        number = randint(1, 1000)
        expression = f'{number}'
        right_answer = returns_right_answer_round(number)
        expressions.append(expression)
        right_answers.append(right_answer)
    return right_answers, expressions


question = 'Answer "yes" if the number is even, otherwise answer "no".'
