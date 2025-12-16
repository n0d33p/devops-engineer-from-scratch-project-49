import random

RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 50
OPERATIONS = ['+', '-', '*']


def calculate(num1: int, num2: int, operator: str) -> int:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        raise ValueError(f"Unknown operator: {operator}")


def generate_round() -> tuple[str, str]:
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATIONS)
    
    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate(num1, num2, operator))
    
    return question, correct_answer