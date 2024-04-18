from brain_games.games.engine import engine_game
from brain_games.games.calc import right_answer_game


def main():
    question = 'What is the result of the expression?'
    right_answer_game()
    engine_game(question)


if __name__ == '__main__':
    main()
