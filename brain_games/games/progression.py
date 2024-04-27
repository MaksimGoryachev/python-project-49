from random import randint


def returns_right_answer_round(len_prog, step_prog, start_prog,
                               number_missing_element) -> tuple:
    expression = ''

    for i in range(len_prog):
        if i != number_missing_element:
            expression += str(start_prog + i
                              * step_prog) + " "
        else:
            expression += ".." + " "
            right_answer = start_prog + i * step_prog

    return right_answer, expression


def generate_data_for_game() -> tuple:
    len_progression = randint(5, 10)
    step_progression = randint(1, 10)
    start_progression = randint(1, 20)
    number_missing_element = randint(0, len_progression - 1)

    return returns_right_answer_round(len_progression,
                                      step_progression,
                                      start_progression,
                                      number_missing_element)


question = 'What number is missing in the progression?'
