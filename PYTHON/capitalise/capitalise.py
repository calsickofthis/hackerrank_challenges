#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    print(s)
    s = s.split(' ')
    
    correct = ''
    for words in s:
        correct = correct + words.capitalize() + ' '
    return correct

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
