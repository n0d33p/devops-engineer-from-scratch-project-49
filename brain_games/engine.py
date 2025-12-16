import prompt

ROUNDS_COUNT = 3


def run_game(name: str, generate_question_func) -> bool:
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_question_func()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer.lower() == correct_answer.lower():
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return False
        
    print(f'Congratulations, {name}!')
