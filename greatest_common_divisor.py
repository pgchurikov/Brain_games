import random


a = 0
b = 0


def gcd(a, b):
    print('Which is the greatest common divisor for these numbers?')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        answer = a + b
        print(f'Question: {a}, {b}')
        user_answer = int(input('Your answer '))
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print('Wrong!')
            print('Let\'s play again')
            break


gcd(a, b)
