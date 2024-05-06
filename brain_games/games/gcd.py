from random import randint


QUESTION = 'Find the greatest common divisor of given numbers.'

NUMBER_1_MAX = 50
NUMBER_2_MAX = 50


def get_greatest_common_divisor(num_1, num_2) -> int:

    for divisor in range(min(num_1, num_2), 0, -1):
        if num_1 % divisor == 0 and num_2 % divisor == 0:
            return divisor


def generate_data_for_game() -> tuple:

    number_1 = randint(1, NUMBER_1_MAX)
    number_2 = randint(1, NUMBER_2_MAX)

    expression = f'{number_1} {number_2}'

    if number_1 == number_2:
        return number_1, expression

    right_answer = get_greatest_common_divisor(number_1, number_2)

    return right_answer, expression
