import prompt

ROUNDS_COUNT = 3


def run_game(game_rules: str, generate_round_func) -> bool:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
    print(game_rules)
    
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_round_func()
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
    return True
