import random

from brain_games.cli import welcome_user
from brain_games.result_of_game import result_of_game


def main():
    correct_answers = 0
    name = welcome_user()
    print('What number is missing in the progression?')
    while correct_answers != 3:
        array_lenght = random.randint(5, 10)
        index_of_missed_element = random.randint(1, array_lenght-1)
        progression = random.randint(1, 10)
        start = random.randint(1, 100)
        array_progression = [str(start)]
        for i in range(1, array_lenght):
            if i == index_of_missed_element:
                array_progression.append('..')
            else:
                array_progression.append(str(start + progression * i))
        print(f'Question: {" ".join(array_progression)}')
        answer = input('Your answer: ')
        true_answer = start + progression * index_of_missed_element
        if int(answer) == true_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}'is wrong answer ;(. Correct answer was '{true_answer}'.")
            break
    result_of_game(correct_answers, name)


if __name__ == '__main__':
    main()
