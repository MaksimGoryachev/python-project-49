#!/usr/bin/env python3


from brain_games.games.engine import engine_game
from brain_games.games.prime import right_answer_game


def main():
    question = 'Answer "yes" if giwen number is prime. Otherwise answet "no"'
    right_answer_game()
    engine_game(question)


if __name__ == '__main__':
    main()
