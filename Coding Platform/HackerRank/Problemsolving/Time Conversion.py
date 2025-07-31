#!/bin/python3

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
    # Write your code here
    
    Time = s[:-2].split(":")      
    if(s[-2:] == "PM"):
        t = int(Time[0])+12
        if(t == 24):
            t = 12
        Time[0] = str(t)
    elif(Time[0] == "12"):
        Time[0] = "00"
    return ":".join(Time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
