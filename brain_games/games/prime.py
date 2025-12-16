import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100
PRIME_PROBABILITY = 0.5


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True


def generate_round() -> tuple[str, str]:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    
    return question, correct_answer