from random import randint


def right_answer_game():
    len_progression = randint(5, 10)
    step_progression = randint(1, 10)
    start = randint(1, 20)
    number_missing_element = randint(0, len_progression - 1)
    expression = ''
    for i in range(len_progression):
        if i != number_missing_element:
            expression = expression + str(start + i * step_progression) + " "
        else:
            expression = expression + ".." + " "
            right_answer = start + i * step_progression
    return right_answer, expression
