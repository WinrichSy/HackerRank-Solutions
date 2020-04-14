#Breaking the Records
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    score_record = list(scores)
    records_array = [0,0]
    minum = score_record[0]
    maximum = score_record[0]
    for i in score_record:
        if i < minum:
            records_array[1] += 1
            minum = i
        elif i > maximum:
            records_array[0] += 1
            maximum = i
    return records_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
