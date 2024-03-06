import random

FIRST_SENTENCE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generation_question_and_answer():

    question_number = random.randint(0, 100)
    question = f'{question_number}'

    true_answer = 'yes' if question_number % 2 == 0 else 'no'

    return question, true_answer
