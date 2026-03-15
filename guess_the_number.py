# guess_the_number.py
# Guessing game using flow control concepts from Chapter 2

import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # Correct guess! Exit the loop.

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
