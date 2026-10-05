# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-09-21
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file
x = input("Input a number:\n> ")

type(x)

x = int(x)

if x >= 6:
    print("x is greater than (or equal to) 6.")
    # print("x is greater than 6!")
    # print("6! is 720")
else:
    print("x is not greater than (or equal to) 6.")

if x >= 4 and x < 12:
    print("x is greater than (or equal to) 4 and less than 12.")

"""Here's a function that gets the type of an object via `type()`
and returns it as a string."""
def _get_type(x):
    return type(x).__name__
    # This also works: return str(type(x))[8:-2]