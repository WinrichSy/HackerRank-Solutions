#Between Two Sets
#https://www.hackerrank.com/challenges/between-two-sets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    in_between = True
    total = 0
    for i in range(a[-1],b[0]+1):
        in_between = True
        for j in a:
            if i%j!=0:
                in_between = False

        if in_between:
            for k in b:
                if k%i!=0:
                    print(f'i: {i}; j: {j}; k:{k}')
                    in_between = False

        if in_between:
            print(i)
            total += 1

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
