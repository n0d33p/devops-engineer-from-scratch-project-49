import sys

from brain_games.cli import welcome_user
from brain_games.module import greet


def show_help():
    help_text = """
Brain Games - a collection of math brain games

Usage: brain-games [OPTIONS]

Options:
  --help  Show this message and exit.

Available games:
  brain-even        Determine if a number is even or odd
  brain-calc        Calculate the result of an expression  
  brain-gcd         Find the greatest common divisor
  brain-progression Find the missing number in a progression
  brain-prime       Determine if a number is prime

Examples:
  brain-even        Start the "Even number" game
  brain-calc        Start the "Calculator" game
  brain-gcd         Start the "GCD" game
  brain-progression Start the "Progression" game
  brain-prime       Start the "Prime number" game
"""
    print(help_text.strip())
    sys.exit(0)


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ['--help', '-h', 'help']:
            show_help()
        else:
            print(f"Unknown option: {arg}")
            print("Try 'brain-games --help' for more information.")
            sys.exit(1)
    
    greet()
    welcome_user()
    print("Choose a game to play:")
    print("  - brain-even")
    print("  - brain-calc") 
    print("  - brain-gcd")
    print("  - brain-progression")
    print("  - brain-prime")