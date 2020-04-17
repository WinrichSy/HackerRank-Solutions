#Beautiful Days at the Movies
#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    days = 0
    for num in range(i, j+1):
        opposite = int(str(num)[::-1])
        if (abs(num-opposite)/k)%1==0:
            days+=1

    return days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
