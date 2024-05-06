from random import randrange


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

NUMBER_MAX = 50


def is_prime(num: int) -> bool:

    if num < 2:
        return False

    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False

    return True


def returns_answer(num):
    return 'yes'if is_prime(num) else 'no'


def generate_data_for_game() -> tuple:

    number = randrange(NUMBER_MAX)

    expression = f'{number}'
    right_answer = returns_answer(number)

    return right_answer, expression
