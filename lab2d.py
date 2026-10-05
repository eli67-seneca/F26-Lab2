# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-09-21
# Purpose: Learn how to use command-line arguments.
# Usage: ./lab2d.py

import sys

# TO DO 1: copy the required lines from README.md to print version, platform, argv and the length of argv.
# run the script in the terminal using command: python ./lab2d.py

print(sys.version)      # Prints version of Python currently in use.
print(sys.platform)     # Prints name of OS
print(sys.argv)         # Prints list of all args given at command-line
print(len(sys.argv))    # Returns number of command-line args given from the terminal

# TO DO 2: copy the required lines from README.md to print argv[0], argv[1] and argv[2]
# run the script using the following command: python lab2d.py maija Maija

print(sys.argv[0])      # Prints the first arg, the name of the script
print(sys.argv[1])      # Prints the second arg
print(sys.argv[2])      # Prints the third arg
print(len(sys.argv))    # Tells us the number of command-line args given from the terminal

explanation = """The script itself is the 'zeroth' command-line argument, which is such because
without the existence of the script, you cannot input any arguments at all."""
print(explanation)