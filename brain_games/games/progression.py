import random

RULES = 'What number is missing in the progression?'


def get_question_and_answer():

    lenght = random.randint(5, 10)
    index_of_missed_element = random.randrange(1, lenght)
    progression = random.randint(1, 10)
    start = random.randint(1, 100)
    end = start + progression * lenght

    subsequence = list((range(start, end, progression)))
    for i in range(0, len(subsequence)):
        subsequence[i] = str(subsequence[i])

    correct_answer = subsequence[index_of_missed_element]
    subsequence[index_of_missed_element] = '..'

    question = " ".join(subsequence)

    return question, correct_answer
