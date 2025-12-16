import random

RULES = 'What number is missing in the progression?'
MIN_START = 1
MAX_START = 50
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGTH = 5
MAX_LENGTH = 15
HIDDEN_ELEMENT = ".."


def generate_progression(start: int, step: int, length: int) -> list[int]:
    return [start + i * step for i in range(length)]


def generate_round() -> tuple[str, str]:
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = HIDDEN_ELEMENT
    
    question = " ".join(str(x) for x in progression)
    
    return question, correct_answer