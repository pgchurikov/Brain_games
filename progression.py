import random

answer = 0
a = 0
b = 0
list = []
index = 0


def progression(a, b, list):
    print('What number is missing in this progression?')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        index = random.randint(0, 7)
        for _ in range(1, 9):
            list.append(a)
            a += b
        answer = list[index]
        list[index] = '..'
        print(f'Question:  {list}')
        user_answer = int(input('Your answer '))
        if user_answer == answer:
            print('Correct!')
            corrects += 1
            list.clear()
        else:
            print('Wrong!')
            print('Let\'s play again')
            break


progression(a, b, list)
