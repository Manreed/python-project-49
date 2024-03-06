import random

FIRST_SENTENCE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generation_question_and_answer():

    number = random.randint(0, 100)
    question = f'{number}'

    true_answer = 'yes' if is_prime(number) else 'no'

    return question, true_answer


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

