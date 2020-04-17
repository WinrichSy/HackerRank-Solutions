#Counting Valleys
#https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    vallies = 0
    level = 0
    in_valley = False
    for i in s:
        if i == 'U':
            level += 1
        elif i == 'D':
            level -= 1
        if level < 0:
            in_valley = True
        elif level > 0:
            in_valley = False
        if in_valley and level == 0:
            vallies += 1
    return vallies

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
