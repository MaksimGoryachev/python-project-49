from random import randint, choice
import prompt


def main():
    question = 'What is the result of the expression?'
    answer_game(question)


def right_answer_game():
    number_1 = randint(1, 50)
    number_2 = randint(1, 50)
    operation = choice(['+', '-', '*'])
    expression = f'{number_1} {operation} {number_2}'
    if operation == '+':
        right_answer = number_1 + number_2
    elif operation == '-':
        right_answer = number_1 - number_2
    else:
        right_answer = number_1 * number_2
    return right_answer, expression


def answer_game(question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    correct_answers_count = 0
    for _ in range(3):
        right_answer, expression = right_answer_game()
        print(f"Question: {expression}")
        geted_answer = input('Your answer: ')
        if str(right_answer) == str(geted_answer):
            print('Correct!')
            correct_answers_count += 1
            if correct_answers_count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'"{geted_answer}" is wrong answer ;(. Correct answer '
                  f'was "{right_answer}".\n Let\'s try'
                  f'again, {name}!')
            break


if __name__ == '__main__':
    main()
