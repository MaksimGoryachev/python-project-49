#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.even import generate_data_for_game, question


def main():
    expressions, right_answers = generate_data_for_game()
    engine_game(question, expressions, right_answers)


if __name__ == '__main__':
    main()
