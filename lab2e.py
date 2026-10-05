# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-09-21
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

import sys

len_argv = len(sys.argv) - 1
print(f"python ", end="")
print(*sys.argv)
print("output: ", end="")

if len_argv == 0:
    print("This script requires exactly two arguments. No arguments were provided!")
elif len_argv == 2:
    print("Hello user, good job, you provided two arguments!")
else:
    print(f"This script requires exactly 2 arguments. You provided {len_argv} arguments.")