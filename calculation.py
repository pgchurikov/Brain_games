import random
from decimal import Decimal


answer = 0
a = 0
b = 0
operator = ''


def calculation(a, operator, b):
    print('Result of calculation')
    corrects = 0
    while corrects < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator_list = ['+', '-', '/', '*']
        operator = random.choice(operator_list)
        if operator == '+':
            answer = a + b
        elif operator == '-':
            answer = a - b
        elif operator == '/':
            answer = Decimal(a / b)
            return (round(answer, 2))
        else:
            answer = a * b
        print(f'Question: {a} {operator} {b} = ..')
        user_answer = float(input('Your answer '))
        if user_answer == answer:
            print('Correct!')
            corrects += 1
        else:
            print('Wrong!')
            print('Let\'s play again')
            break


calculation(a, operator, b)
