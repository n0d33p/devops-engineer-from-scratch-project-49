from brain_games.engine import run_game
from brain_games.games.even import RULES, generate_round


def main() -> None:
    run_game(RULES, generate_round)