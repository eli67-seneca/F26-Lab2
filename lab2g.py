# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

x = 3
if x < 6:
    if x > 2:
        print("x is less than 6 and x is greater than 2.")

income = int(input("Input income:\n> "))
status = input("Input status:\n> ").casefold()
tax = None

SINGLE = "Single"
MARRIED = "Married"

# I should probably sanitise my inputs
if status.startswith('s'):
    status = SINGLE
elif status.startswith('m'):
    status = MARRIED

if status == SINGLE:
    if income <= 32_000:
        tax = income * 0.1
    else:
        tax = 3_200 + income * 0.25
elif status == MARRIED:
    if income <= 64_000:
        tax = income * 0.1
    else:
        tax = 6_400 + income * 0.25

print(f"Income:\t${income:,}\nStatus:\t{status}\nTax:\t${tax:,}")