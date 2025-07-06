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
    s = [0,0,0]
    for i in arr:
        if(i > 0):
            s[0] += 1
        elif(i < 0):
            s[1] += 1
        else:
            s[2] += 1
    L = len(arr)
    for i in s:
        print(f"{i/L:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
