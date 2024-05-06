#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.even import QUESTION, generate_data_for_game


def main():
    engine_game(QUESTION, generate_data_for_game)


if __name__ == '__main__':
    main()
