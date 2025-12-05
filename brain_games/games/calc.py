import random

RULES = 'What is the result of the expression?'


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        raise ValueError(f"Unknown operator: {operator}")
    

def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])

    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate(num1, num2, operator))

    return question, correct_answer