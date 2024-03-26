import random
import math


a = 0


def is_prime(a):
    print('Is this number prime? y/n')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        answer = 'y'
        if a <= 1:
            answer = 'n'
        i = 2
        while i <= math.sqrt(a):
            if a % i == 0:
                answer = 'n'
                break
            i += 1
        print(f'Question: {a}')
        user_answer = input('Your answer ')
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print('Wrong!')
            print('Let\'s play again')
            break


is_prime(a)
