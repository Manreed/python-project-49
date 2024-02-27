import random

FIRST_SENTENCE = 'What number is missing in the progression?'


def generation_question_and_answer():

    array_lenght = random.randint(5, 10)
    index_of_missed_element = random.randint(1, array_lenght - 1)
    progression = random.randint(1, 10)
    start = random.randint(1, 100)
    array_progression = [str(start)]

    for i in range(1, array_lenght):
        if i == index_of_missed_element:
            array_progression.append('..')
        else:
            array_progression.append(str(start + progression * i))

    question = f'{" ".join(array_progression)}'
    true_answer = start + progression * index_of_missed_element

    return question, true_answer
