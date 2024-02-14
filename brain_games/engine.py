import prompt
CORRECT_ANSWERS = 3
BEGINNING_OF_QUESTION = 'Question: '


def launch_of_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.first_sentence)
    for i in range(1, CORRECT_ANSWERS + 1):
        question, true_answer = game.generation_question_and_answer()
        print(BEGINNING_OF_QUESTION + question)
        answer = input('Your answer: ')
        if answer == str(true_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer is '{true_answer}'")
            print(f"Let's try again, {name}!")
            break
        if i == CORRECT_ANSWERS:
            print(f'Congratulations, {name}!')
