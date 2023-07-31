#!/bin/python3

from datetime import datetime
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    print(s)
    t = datetime.strptime(s, '%I:%M:%S%p')
    # Format the datetime object into a 24-hour time string
    print(t.strftime('%H:%M:%S'))
    return t.strftime('%H:%M:%S')

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()
