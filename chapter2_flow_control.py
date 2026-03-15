# ============================================================
# CHAPTER 2: FLOW CONTROL - All Code Examples
# Automate the Boring Stuff with Python by Al Sweigart
# ============================================================


# ------------------------------------------------------------
# 1. BOOLEAN VALUES
# File concept: boolean_values.py
# ------------------------------------------------------------
print("=== Boolean Values ===")
spam = True
print(spam)          # True

spam = False
print(spam)          # False


# ------------------------------------------------------------
# 2. COMPARISON OPERATORS
# File concept: comparison_operators.py
# ------------------------------------------------------------
print("\n=== Comparison Operators ===")
print(42 == 42)      # True
print(42 == 99)      # False
print(2 != 3)        # True
print(2 != 2)        # False
print(1 < 2)         # True
print(2 < 1)         # False
print(1 > 2)         # False
print(5 >= 5)        # True
print(5 <= 4)        # False

# Comparing strings
print('hello' == 'hello')   # True
print('hello' == 'Hello')   # False (case sensitive)
print('hello' != 'world')   # True


# ------------------------------------------------------------
# 3. BOOLEAN OPERATORS: and, or, not
# File concept: boolean_operators.py
# ------------------------------------------------------------
print("\n=== Boolean Operators ===")

# and operator (both must be True)
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# or operator (at least one must be True)
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# not operator (inverts the Boolean)
print(not True)         # False
print(not False)        # True
print(not not True)     # True


# ------------------------------------------------------------
# 4. MIXING BOOLEAN AND COMPARISON OPERATORS
# File concept: mixing_operators.py
# ------------------------------------------------------------
print("\n=== Mixing Boolean and Comparison Operators ===")
myAge = 26
myPet = 'cat'

print((myAge > 17) and (myPet == 'cat'))   # True and True -> True
print((myAge > 17) and (myPet == 'dog'))   # True and False -> False
print((1 == 2) or (2 == 2))               # False or True -> True
print(not (1 == 2))                        # not False -> True


# ------------------------------------------------------------
# 5. IF STATEMENTS
# File concept: if_statements.py
# ------------------------------------------------------------
print("\n=== if Statements ===")
name = 'Alice'

if name == 'Alice':
    print('Hi, Alice.')

# With else
password = 'swordfish'
if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password.')

# With elif
name = 'Bob'
age = 5

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')


# ------------------------------------------------------------
# 6. WHILE LOOP - Basic
# File concept: while_loop.py
# ------------------------------------------------------------
print("\n=== while Loop ===")
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1


# ------------------------------------------------------------
# 7. AN ANNOYING WHILE LOOP (name input example)
# File concept: your_name.py
# ------------------------------------------------------------
print("\n=== your_name.py (simulated) ===")
# Original requires input(); simulated here with a preset value
name = ''
# In real version: while name != 'your name':
#                      name = input('Please type your name.')
# Simulated:
name = 'your name'
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')


# ------------------------------------------------------------
# 8. BREAK STATEMENT
# File concept: your_name_break.py
# ------------------------------------------------------------
print("\n=== break Statement ===")
# Original loops until user types 'your name'
# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!')
# Simulated:
print("(break example: exits loop when condition met)")


# ------------------------------------------------------------
# 9. CONTINUE STATEMENT
# File concept: spam_continue.py
# ------------------------------------------------------------
print("\n=== continue Statement ===")
# Original:
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue          # goes back to start of loop
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')
print("(continue example: skips back to loop start if name != 'Joe')")


# ------------------------------------------------------------
# 10. TRUTHY AND FALSY VALUES
# File concept: truthy_falsy.py
# ------------------------------------------------------------
print("\n=== Truthy and Falsy Values ===")
# These values are considered False in a Boolean context:
# 0, 0.0, '' (empty string), [], {}, None
# Everything else is True

name = ''
while not name:          # loops while name is empty (falsy)
    # name = input('Enter your name: ')
    name = 'Alice'       # simulated
print('How many guests will you have?')
# numOfGuests = int(input())
numOfGuests = 0          # simulated
if numOfGuests:          # falsy if 0
    print('Be sure to have enough room for all your guests.')
print('Done')


# ------------------------------------------------------------
# 11. FOR LOOP AND range()
# File concept: for_loop.py
# ------------------------------------------------------------
print("\n=== for Loop and range() ===")

# Basic for loop
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# range() with start, stop, step
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# range() counting down
for i in range(5, -1, -1):  # 5, 4, 3, 2, 1, 0
    print(i)


# ------------------------------------------------------------
# 12. EQUIVALENT WHILE LOOP (same as for loop above)
# File concept: while_equivalent.py
# ------------------------------------------------------------
print("\n=== while equivalent of for loop ===")
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1


# ------------------------------------------------------------
# 13. SUM WITH FOR LOOP
# File concept: sum_loop.py
# ------------------------------------------------------------
print("\n=== Sum with for loop ===")
total = 0
for num in range(101):    # 0 to 100
    total = total + num
print(total)              # 5050


# ------------------------------------------------------------
# 14. IMPORTING MODULES
# File concept: import_example.py
# ------------------------------------------------------------
print("\n=== Importing Modules ===")
import random

for i in range(5):
    print(random.randint(1, 10))   # prints 5 random numbers 1-10


# ------------------------------------------------------------
# 15. FROM IMPORT STATEMENT
# File concept: from_import_example.py
# ------------------------------------------------------------
print("\n=== from import Statement ===")
from random import randint  # import just the randint function

for i in range(5):
    print(randint(1, 10))   # can call directly without 'random.'


# ------------------------------------------------------------
# 16. sys.exit() - ENDING A PROGRAM EARLY
# File concept: sysexit_example.py
# ------------------------------------------------------------
print("\n=== sys.exit() Example ===")
import sys

# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')
print("(sys.exit() example: call sys.exit() to stop program immediately)")


# ============================================================
# STANDALONE PROGRAMS (save each as its own .py file)
# ============================================================

# ------------------------------------------------------------
# STANDALONE: guess_the_number_preview.py
# A guessing game using while loop and if/elif/else
# (Full version is in Chapter 3, but flow control shown here)
# ------------------------------------------------------------
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())
#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high.')
#     else:
#         break
# if guess == secretNumber:
#     print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))
