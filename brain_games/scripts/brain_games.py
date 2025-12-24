import sys
import prompt


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h']:
        print("Usage: brain-games")
        print("\nBrain Games - a collection of math brain games")
        print("\nAvailable games:")
        print("  • brain-even        - Determine if a number is even or odd")
        print("  • brain-calc        - Calculate the result of an expression")
        print("  • brain-gcd         - Find the greatest common divisor")
        print("  • brain-progression - Find the missing number in "
              "a progression")
        print("  • brain-prime       - Determine if a number is prime")
        print("\nRun any game with: brain-<game_name>")
        sys.exit(0)
    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
    print("\nAvailable games:")
    print("  • brain-even        - Determine if a number is even or odd")
    print("  • brain-calc        - Calculate the result of an expression")
    print("  • brain-gcd         - Find the greatest common divisor")
    print("  • brain-progression - Find the missing number in "
          "a progression")
    print("  • brain-prime       - Determine if a number is prime")
    print("\nRun any game with: brain-<game_name>")