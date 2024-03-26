import random
from calculation import calculation
from progression import progression
from odd_number import is_odd
from greatest_common_divisor import gcd
from prime_number import is_prime


print('brain-progression')
print('Welcome to the Brain Game!')


corrects = 0
games = [calculation, progression, is_odd, gcd, is_prime]
random_game = random.choice(games)


name = input('May I have your name? ')
print(f'Hello, {name}!')


print(random_game)


if corrects == 3:
    print(f'Congratulations, {name}!')
