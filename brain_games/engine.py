import prompt

ROUNDS_COUNT = 3


def launch_of_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)

    for i in range(ROUNDS_COUNT):

        question, correct_answer = game.get_question_and_answer()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')

        if answer != str(correct_answer):
            return (f"'{answer}' is wrong answer ;(."
                    f" Correct answer is '{correct_answer}'\n"
                    f"Let's try again, {name}!")

        print('Correct!')

    return f'Congratulations, {name}!'
