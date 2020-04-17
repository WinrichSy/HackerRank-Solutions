#Repeated String
https://www.hackerrank.com/challenges/repeated-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_counts = s.count('a')
    div, rem = divmod(n, len(s))
    if rem>0:
        return(a_counts*div) + (s[:rem].count('a'))
    else:
        return(a_counts*div)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
