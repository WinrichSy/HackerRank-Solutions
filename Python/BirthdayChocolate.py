#Birthday Chocolate
#https://www.hackerrank.com/challenges/the-birthday-bar/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    bars_array = list(s)
    diff_ways = 0
    for idx, elm in enumerate(bars_array):
        total = 0
        if idx+m <= len(bars_array):
            print(f'idx+m: {idx+m}; len(bars_array): {len(bars_array)}')
            for j in range(m):
                total += bars_array[idx+j]
            if total == d:
                diff_ways += 1

    return diff_ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
