#Minimum Distances
#https://www.hackerrank.com/challenges/minimum-distances/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    if len(a) == 1:
        return -1
    if a[0]==a[1]:
        return 1
    minimum = len(a)-1
    for i in range(len(a)-1):
        for j in range(i+1, len(a)-1):
            if a[i]==a[j]:
                if j-i < minimum:
                    minimum = j-i
                    if minimum == 1:
                        return 1

    if minimum == len(a)-1:
        return -1
    return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
