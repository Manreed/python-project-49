from brain_games import cli
from brain_games import result_of_game


def engine(game):
    correct_answers = 0
    name = cli.welcome_user()
    print(game.first_sentence)
    while correct_answers != 3:
        question, true_answer = game.generation_question_and_answer()
        print(question)
        answer = input('Your answer: ')
        if answer == str(true_answer):
            correct_answers += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer is '{true_answer}'")
            break
    result_of_game.result_of_game(correct_answers, name)
