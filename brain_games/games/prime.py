import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():

    number = random.randint(0, 100)
    question = f'{number}'

    correct_answer = 'yes' if is_prime(number) else 'no'

    return question, correct_answer


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True
