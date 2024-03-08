import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():

    question_number = random.randint(0, 100)
    question = f'{question_number}'

    correct_answer = 'yes' if question_number % 2 == 0 else 'no'

    return question, correct_answer
