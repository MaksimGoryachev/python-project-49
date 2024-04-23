from brain_games.engine import engine_game
from brain_games.games.calc import generate_data_for_game


def main():
    question, right_answers, expressions = generate_data_for_game()
    engine_game(question, right_answers, expressions)


if __name__ == '__main__':
    main()
