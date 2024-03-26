import random


a = 0


def is_odd(a):
    print('Is this number odd? y/n')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        if a % 2 == 0:
            answer = 'y'
        else:
            answer = 'n'
        print(f'Question: {a}')
        user_answer = input('Your answer ')
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print('Wrong!')
            print('Let\'s play again')
            break


is_odd(a)
