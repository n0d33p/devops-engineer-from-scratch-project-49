import random

RULES = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression


def generate_round():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 15)

    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression[hidden_index])

    progression_str = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            progression_str.append("..")
        else:
            progression_str.append(str(num))

    question = " ".join(progression_str)

    return question, correct_answer