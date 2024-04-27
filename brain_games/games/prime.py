from random import randint


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return True


def returns_right_answer_round(num):
    return 'yes'if is_prime(num) else 'no'


def generate_data_for_game() -> tuple:
    number = randint(2, 101)
    expression = f'{number}'
    right_answer = returns_right_answer_round(number)
    return right_answer, expression


question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
