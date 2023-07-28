#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_num, negative_num, zero_num = 0, 0, 0

    for entry in arr:
        if entry > 0: positive_num += 1
        if entry < 0: negative_num += 1
        if entry == 0: zero_num += 1
        
    print("{:.6f}".format(positive_num / len(arr)))
    print("{:.6f}".format(negative_num / len(arr)))
    print("{:.6f}".format(zero_num / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
