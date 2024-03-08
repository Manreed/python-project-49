import random
import operator

RULES = 'What is the result of the expression?'


def get_question_and_answer():

    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    math_symbols = [('+', operator.add),
                    ('-', operator.sub),
                    ('*', operator.mul)]

    operation, method = random.choice(math_symbols)
    question = f'{first_number} {operation} {second_number}'

    correct_answer = method(first_number, second_number)

    return question, correct_answer
