# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-09-21
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file
import sys

# You did say "EXACT OUTPUT"
print("python ", end="")
print(*sys.argv)
print("output: ", end="")

len_argv = len(sys.argv) - 1

if len_argv < 2:
    print("The script requires at least 2 arguments.")
else:
    name = sys.argv[1]
    age = sys.argv[2]
    s = "s" if age != 1 else ""
    print(f"Hi {name}, you are {age} year{s} old and the script received {len_argv} arguments.")
