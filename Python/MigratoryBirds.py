#Migratory Birds
#https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    highest_type = 1
    highest_count = 0
    for i in range(1,6):
        if arr.count(i)>highest_count:
            highest_count = arr.count(i)
            highest_type = i

    return highest_type


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
