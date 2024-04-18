#!/usr/bin/env python3


from brain_games.games.engine import engine_game
from brain_games.games.progression import right_answer_game


def main():
    question = 'What number is missing in the progression?'
    right_answer_game()
    engine_game(question)


if __name__ == '__main__':
    main()
