import random

from brain_games.cli import welcome_user
from brain_games.result_of_game import result_of_game


def main():
    correct_answers = 0
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while correct_answers != 3:
        number = random.randint(2, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        if (is_prime(number) == True and answer == 'yes') or (is_prime(number) == False and answer == 'no'):
            correct_answers += 1
            print('Correct')
        else:
            if is_prime(number):
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
            break
    result_of_game(correct_answers, name)


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
