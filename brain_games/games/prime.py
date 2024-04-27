from random import randint


def is_prime(num: int) -> bool:
    for _ in range(2, num // 2 + 1):
        return num % _ == 0


def returns_right_answer_round(num):
    return 'no'if is_prime(num) else 'yes'


def generate_data_for_game() -> tuple:
    number = randint(2, 101)
    expression = f'{number}'
    right_answer = returns_right_answer_round(number)
    return right_answer, expression


question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
