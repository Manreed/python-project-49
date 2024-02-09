import random

first_sentence = 'Answer "yes" if the number is even, otherwise answer "no".'


def generation_question_and_answer():
    question_number = random.randint(0, 100)
    question = f'Question: {question_number}'
    if question_number % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return question, true_answer
