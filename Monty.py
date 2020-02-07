# Ok, as my first real self-directed program, I want to see if I can
# create a 'random' question asker, in the form of the sooth sayer from python's holy grail.

# The thinking is that I will import the random function to generate a number between 1 and 100
# and use this to pick from a list of pre-populated questions with nested if statements.

# At a later date I am sure that I will be able to have a full SQL Q&A database which I will pull from for a bit of
# fun, but for now I am looking at a list of if functions.

import random

question = random.randrange(100)

name = str(input("What is your name? "))
quest = str(input("What is your quest?"))
print(question  )