#Strings: Making Anagrams
#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    total = 0
    total_set = sorted(list(set(a+b)))
    for i in total_set:
        total += abs(a.count(i)-b.count(i))
    return total

if  __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
