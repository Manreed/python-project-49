import random

FIRST_SENTENCE = 'Find the greatest common divisor of given numbers.'


def generation_question_and_answer():

    true_answer = 0
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'
    gcd = min(first_number, second_number)

    while true_answer == 0:
        if first_number % gcd == 0 and second_number % gcd == 0:
            true_answer = gcd
        else:
            gcd -= 1

    return question, true_answer
