from brain_games.cli import greet, welcome_user
from brain_games.engine import run_game
from brain_games.games.calc import RULES, generate_round


def main() -> None:
    greet()
    name = welcome_user()
    print(RULES)
    run_game(name, generate_round)