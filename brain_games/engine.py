import prompt

NUMBER_OF_ROUNDS = 3


def engine_game(question, generate_data_for_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    correct_answers_count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        right_answer, expression = generate_data_for_game()
        print(f"Question: {expression}")
        geted_answer = prompt.string('Your answer: ')
        if str(right_answer) == str(geted_answer):
            print('Correct!')
            correct_answers_count += 1
            if correct_answers_count == NUMBER_OF_ROUNDS:
                print(f'Congratulations, {name}!')
        else:
            print(f'"{geted_answer}" is wrong answer ;(. Correct answer '
                  f'was "{right_answer}".\n Let\'s try'
                  f' again, {name}!')
            break
