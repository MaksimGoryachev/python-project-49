#!/usr/bin/env python3


from brain_games.engine import engine_game
from brain_games.games.gcd import right_answer_game


def main():
    question = 'Find the greatest common divisor of given numbers.'
    right_answers, expressions = right_answer_game()
    engine_game(question, right_answers, expressions)


if __name__ == '__main__':
    main()
