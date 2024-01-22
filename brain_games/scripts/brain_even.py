import random
from brain_games.cli import welcome_user
from brain_games.result_of_game import result_of_game


def main():
    correct_answers = 0
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers != 3:
        question_number = random.randint(0, 100)
        print(f'Question: {question_number}')
        answer = input('Your answer: ')
        if (question_number % 2 == 0 and answer == 'yes') or (question_number % 2 == 1 and answer == 'no'):
            print('Correct')
            correct_answers += 1
        else:
            correct_answers = 0
            if question_number % 2 == 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                break
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                break
    result_of_game(correct_answers, name)


if __name__ == '__main__':
    main()
