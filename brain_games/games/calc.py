import random
import operator

FIRST_SENTENCE = 'What is the result of the expression?'


def generation_question_and_answer():

    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    math_symbols = [('+', operator.add(first_number, second_number)),
                    ('-', operator.sub(first_number, second_number)),
                    ('*', operator.mul(first_number, second_number))]
    rand_operation_and_symbol = math_symbols[random.randint(0, 2)]
    question = f'{first_number} {rand_operation_and_symbol[0]} {second_number}'

    true_answer = rand_operation_and_symbol[1]

    return question, true_answer
