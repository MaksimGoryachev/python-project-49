from random import randint


def returns_right_answer_round(num_1, num_2) -> int:
    for divisor in range(min(num_1, num_2), 0, -1):
        if num_1 % divisor == 0 and num_2 % divisor == 0:
            return divisor


def generate_data_for_game() -> tuple:
    number_1 = randint(1, 50)
    number_2 = randint(1, 50)
    expression = f'{number_1} {number_2}'

    if number_1 == number_2:
        return number_1, expression

    right_answer = returns_right_answer_round(number_1, number_2)

    return right_answer, expression


question = 'Find the greatest common divisor of given numbers.'
