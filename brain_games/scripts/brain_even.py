#!/usr/bin/env python3
from brain_games.engine import engine_game
from brain_games.games.even import generate_data_for_game


def main():
    engine_game(generate_data_for_game)


if __name__ == '__main__':
    main()
