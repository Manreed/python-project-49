import random

FIRST_SENTENCE = 'What is the result of the expression?'
MATH_SYMBOLS = ['+', '-', '*']


def generation_question_and_answer():

    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    rand_symbol = MATH_SYMBOLS[random.randint(0, 2)]
    question = f'{first_number} {rand_symbol} {second_number}'

    match rand_symbol:
        case '+':
            true_answer = first_number + second_number
        case '-':
            true_answer = first_number - second_number
        case '*':
            true_answer = first_number * second_number

    return question, true_answer
