import random
from brain_games.cli import welcome_user
from brain_games.result_of_game import result_of_game


def main():
    correct_answers = 0
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while correct_answers != 3:
        true_answer = 0
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        print(f'Question: {first_number} {second_number}')
        answer = input('Your answer: ')
        gcd = min(first_number, second_number)
        while true_answer == 0:
            if max(first_number, second_number) % gcd == 0 and min(first_number, second_number) % gcd == 0:
                true_answer = gcd
            else:
                gcd -= 1
        if int(answer) == true_answer:
            correct_answers += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
            break

    result_of_game(correct_answers, name)


if __name__ == '__main__':
    main()
