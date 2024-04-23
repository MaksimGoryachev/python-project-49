from random import randint


def right_answer_game():
    right_answers = []
    expressions = []
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        len_progression = randint(5, 10)
        step_progression = randint(1, 10)
        start_progression = randint(1, 20)
        number_missing_element = randint(0, len_progression - 1)
        expression = ''
        for i in range(len_progression):
            if i != number_missing_element:
                expression += str(start_progression + i
                                  * step_progression) + " "
            else:
                expression += ".." + " "
                right_answer = start_progression + i * step_progression
        expressions.append(expression)
        right_answers.append(right_answer)
    return right_answers, expressions
