import random


def main():
    correct_answers = 0
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    math_symbols = ['+', '-', '*']
    while correct_answers != 3:
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 100)
        rand_symbol = math_symbols[random.randint(0, 2)]
        print(f'Question: {first_number} {rand_symbol} {second_number}')
        answer = input('Your answer: ')
        if rand_symbol == '+':
            true_answer = first_number + second_number
            if int(answer) == true_answer:
                print('Correct!')
                correct_answers += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
                break
        elif rand_symbol == '-':
            true_answer = first_number - second_number
            if int(answer) == true_answer:
                print('Correct!')
                correct_answers += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
                break
        elif rand_symbol == '*':
            true_answer = first_number * second_number
            if int(answer) == true_answer:
                print('Correct!')
                correct_answers += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
                break

    if correct_answers == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
