#!/usr/bin/env python3


from brain_games.engine import engine_game
from brain_games.games.prime import right_answer_game


def main():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    right_answers, expressions = right_answer_game()
    engine_game(question, right_answers, expressions)


if __name__ == '__main__':
    main()
