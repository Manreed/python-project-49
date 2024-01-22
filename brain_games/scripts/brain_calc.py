import random
from brain_games.cli import welcome_user
from brain_games.result_of_game import result_of_game


def main():
    correct_answers = 0
    name = welcome_user()
    print('What is the result of the expression?')
    math_symbols = ['+', '-', '*']
    while correct_answers != 3:
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 100)
        rand_symbol = math_symbols[random.randint(0, 2)]
        print(f'Question: {first_number} {rand_symbol} {second_number}')
        answer = input('Your answer: ')
        match rand_symbol:
            case '+':
                true_answer = first_number + second_number
            case '-':
                true_answer = first_number - second_number
            case '*':
                true_answer = first_number * second_number
        if int(answer) == true_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer is '{true_answer}'")
            break

    result_of_game(correct_answers, name)


if __name__ == '__main__':
    main()
