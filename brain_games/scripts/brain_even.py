import random


def main():
    correct_answers = 0
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
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
                print(f"Let's try again, {name}!")
                break
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
