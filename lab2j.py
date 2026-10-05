# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li
# Date: 2026-09-21
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

import math

# TO DO 1: 
# Import the `math` module.
# Define a variable named num. Prompt the user to input a number and assign it to the variable num.
# Convert the user input to a floating-point number and assign it to num.

while True:
    num = float(input("Please input a number: "))

    if num < 0:
        print("Invalid number.")
    elif num == 0:
        print("Exiting...")
        break
    else:
        print(math.sqrt(num))
