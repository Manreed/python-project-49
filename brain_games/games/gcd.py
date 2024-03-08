import random

RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():

    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'

    correct_answer = get_gcd(first_number, second_number)

    return question, correct_answer


def get_gcd(a, b):
    answer = 0
    gcd = min(a, b)
    while answer == 0:
        if a % gcd == 0 and b % gcd == 0:
            answer = gcd
        else:
            gcd -= 1

    return answer
