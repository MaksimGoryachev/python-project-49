from random import randrange


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

NUMBER_MAX = 50


def is_even(num: int) -> bool:
    return num % 2 == 0


def returns_answer(num):
    return 'yes' if is_even(num) else 'no'


def generate_data_for_game():

    number = randrange(NUMBER_MAX)

    expression = f'{number}'
    right_answer = returns_answer(number)

    return right_answer, expression
