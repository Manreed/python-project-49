import random

FIRST_SENTENCE = 'Find the greatest common divisor of given numbers.'


def generation_question_and_answer():

    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'

    true_answer = find_gcd(first_number, second_number)

    return question, true_answer


def find_gcd(a, b):
    answer = 0
    gcd = min(a, b)
    while answer == 0:
        if a % gcd == 0 and b % gcd == 0:
            answer = gcd
        else:
            gcd -= 1

    return answer
