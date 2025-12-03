from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.even import RULES, generate_round
from brain_games.module import greet


def main():
    greet()
    name = welcome_user()
    print(RULES)
    run_game(name, generate_round)