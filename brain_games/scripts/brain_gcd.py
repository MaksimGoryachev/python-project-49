#!/usr/bin/env python3


from brain_games.games.engine import engine_game
from brain_games.games.gcd import right_answer_game


def main():
    question = 'Find the greatest common divisor of given numbers.'
    right_answer_game()
    engine_game(question)


if __name__ == '__main__':
    main()
