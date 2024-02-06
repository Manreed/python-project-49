import random

first_sentence = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generation_question_and_answer():
    number = random.randint(2, 100)
    question = f'Question: {number}'
    if is_prime(number):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return question, true_answer


def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

