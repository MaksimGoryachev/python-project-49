#!/usr/bin/env python3


from brain_games.engine import engine_game
from brain_games.even import right_answer_game


def main():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    right_answer_game()
    engine_game(question)


if __name__ == '__main__':
    main()
