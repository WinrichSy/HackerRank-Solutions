#Find Digits
#https://www.hackerrank.com/challenges/find-digits/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    divisors = list(str(n))
    ans = 0
    for i in divisors:
        if int(i)!=0 and n%int(i)==0:
            ans+=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
