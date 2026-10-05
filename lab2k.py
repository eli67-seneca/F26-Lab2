# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: use for loop.
# Usage: ./lab2k.py

# TO DO 1: 
#Follow the instructions given in the README.md file.
fruits = ["apple", "banana", "cherry", "date"]

# Use a for loop to iterate over the list
#for fruit in fruits:
#    print(fruit)

#for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.
total = 0

for i in range(101):
    if i % 2 == 1:
        continue
    else:
        total += i

# Should be 2550 (Sum_0^{50} 2n = 2550)
print(total)