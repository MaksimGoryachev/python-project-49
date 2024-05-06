from random import randint


QUESTION = 'What number is missing in the progression?'

LENGTH_MIN = 5
LENGTH_MAX = 10

STEP_MIN = 1
STEP_MAX = 10

START_MIN = 1
START_MAX = 20


def missing_element(start_prog, number_missing_element, step_prog) -> tuple:
    return start_prog + number_missing_element * step_prog


def generate_data_for_game() -> tuple:

    len_progression = randint(LENGTH_MIN, LENGTH_MAX)
    step_progression = randint(STEP_MIN, STEP_MAX)
    start_progression = randint(START_MIN, START_MAX)

    number_missing_element = randint(0, len_progression - 1)

    right_answer = missing_element(start_progression, number_missing_element,
                                   step_progression)

    expression = ''
    for i in range(len_progression):
        if i != number_missing_element:
            expression += str(start_progression + i
                              * step_progression) + " "
        else:
            expression += ".." + " "

    return right_answer, expression
