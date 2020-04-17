#Minimum Absolute Difference in an Array
#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    min = abs(sorted_arr[0]-sorted_arr[1])
    for i in range(len(sorted_arr)-1):
        if min > abs(sorted_arr[i]-sorted_arr[i+1]):
            min = abs(sorted_arr[i]-sorted_arr[i+1])
    return min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
