# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use while loops for validating user input.
# Usage: ./lab2i.py

# TO DO 1: 
# Creat variable pin. The value of pin should be a 4 digit code inputted by the user.
# Add a while loop to create program that wont end until the user enters 1234.
# Follow the specific instructions given in the README.md file.
#guess = 5
#number = int(input("Guess what number less than 10 I am thinking off?"))
#while number != guess:  # loop condition 
#  print("incorrect guess, try again...")
# number = int(input("Guess what number less than 10 I am thinking off?")) # keep taking input from user until the user enters the correct guess.
#print("You got it right!") # this statement will be executed when loop has terminated which will only happen when the user enters the number 5.
# Define the correct PIN

pin = 1234
correct = False

while not correct:
    user_input = int(input("Please type in your PIN: "))

    if user_input != pin:
        print("Incorrect...try again\n")
    else:
        print("Correct PIN, You can enter!")
        break

# Oops, I thought I was supposed to implement this.
# from random import randint

# count = randint(1, 10)
# correct = False

# print("I'm thinking of a number between 1 and 10.\n \
#       Can you guess what it is?\n")

# while not correct:
#     guess = int(input("> "))

#     if guess == count:
#         correct = True
#     else:
#         print("That's not correct! Try again.")

# print("You guessed it!")
# print(f"The number I'm thinking of was {count}")