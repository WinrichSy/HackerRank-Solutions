#Divisible Sum Pairs
#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    total = 0
    i = 0
    j = i+1
    while i<len(ar)-1:
        j=i+1
        while j<len(ar):
            if (ar[i]+ar[j])%k == 0:
                total += 1
            j += 1
        i += 1

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
