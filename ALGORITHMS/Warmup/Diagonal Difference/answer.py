#!/bin/python3

import math
import os
import random
import re
import sys
from turtle import right

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # print(arr)

    # left 2 right
    left_to_right = 0
    i = 0
    for _ in arr:
        # print(arr[i][i])
        left_to_right = left_to_right + arr[i][i]
        i += 1
    
    # right 2 left
    right_to_left = 0
    i = 0
    x = n - 1
    for _ in arr:
        # print(arr[i][x])
        right_to_left = right_to_left + arr[i][x]
        x -= 1
        i += 1
    
    # print(f'left to right is : ',left_to_right)
    # print(f'right to left is : ',right_to_left)

    print(right_to_left - left_to_right)

    return right_to_left - left_to_right

    # print(max([left_to_right,right_to_left]) - min([left_right,right_to_left]))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    # fptr.write(str(result) + '\n')

    # fptr.close()